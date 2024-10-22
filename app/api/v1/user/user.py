from fastapi import APIRouter, Query
from app.controllers.user_controller import user_controller
from app.schemas import Success
from app.schemas.user_schemas import *

router = APIRouter()

@router.get("/test", summary="")
async def tets():
    return Success(msg="tets")

@router.get("/getuser", summary="获取用户by userid")
async def getuserbyid(user_id:str = Query(..., description="用户ID")):
    user = await user_controller.get_user(user_id=user_id)
    print("get")
    return Success(data=await user.to_dict())


@router.post("/change", summary="用户修改个人资料")
async def update_user_info(user: UserUpdateRequest):
    # 在这里处理数据库更新逻辑
    success = await user_controller.update_user_in_db(user)  # 伪函数，请自行实现
    if success:
        msg="OK,成功更新"
    return Success(msg=msg)





# @router.get("/list", summary="查看用户列表")
# async def list_users(name: str = Query(None, description="用户名")):
#     users = await user_controller.get_users_by_name(name)
#     return Success(data=users)

# @router.get("/get", summary="查看用户")
# async def get_user(id: int = Query(..., description="用户ID")):
#     user = await user_controller.get(id=id)
#     return Success(data=user)

# @router.post("/create", summary="创建用户")
# async def create_user(user_in: UserCreate):
#     await user_controller.create_user(obj_in=user_in)
#     return Success(msg="Created Successfully")

# @router.post("/update", summary="更新用户")
# async def update_user(user_in: UserUpdate):
#     await user_controller.update_user(obj_in=user_in)
#     return Success(msg="Updated Successfully")

# @router.delete("/delete", summary="删除用户")
# async def delete_user(id: int = Query(..., description="用户ID")):
#     await user_controller.delete_user(user_id=id)
#     return Success(msg="Deleted Successfully")
