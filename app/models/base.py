import asyncio
from datetime import datetime

from tortoise import fields, models

from app.settings import settings


class BaseModel(models.Model):
    # id = fields.BigIntField(pk=True, index=True)
    id = fields.BigIntField()

    async def to_dict(self, m2m: bool = False, exclude_fields: list[str] | None = None):
        if exclude_fields is None:
            exclude_fields = []

        d = {}
        for field in self._meta.db_fields:  # 遍历模型所有字段
            if field not in exclude_fields:  # 跳过需要排除的字段
                value = getattr(self, field)  # 获取字段值
                if isinstance(value, datetime):  # 如果是 datetime 类型，格式化为字符串
                    value = value.strftime(settings.DATETIME_FORMAT)
                d[field] = value  # 将值添加到字典中

        if m2m:  # 如果需要包含多对多字段
            tasks = [
                self.__fetch_m2m_field(field, exclude_fields)
                for field in self._meta.m2m_fields  # 遍历多对多字段
                if field not in exclude_fields
            ]
            results = await asyncio.gather(*tasks)  # 异步地获取所有多对多字段的值
            for field, values in results:
                d[field] = values  # 将多对多字段的值也添加到字典中

        return d  # 返回最终的字典


    async def __fetch_m2m_field(self, field, exclude_fields):
        values = await getattr(self, field).all().values()
        formatted_values = []

        for value in values:
            formatted_value = {}
            for k, v in value.items():
                if k not in exclude_fields:
                    if isinstance(v, datetime):
                        formatted_value[k] = v.strftime(settings.DATETIME_FORMAT)
                    else:
                        formatted_value[k] = v
            formatted_values.append(formatted_value)

        return field, formatted_values

    class Meta:
        abstract = True


class UUIDModel:
    uuid = fields.UUIDField(unique=True, pk=False)


class TimestampMixin:
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
