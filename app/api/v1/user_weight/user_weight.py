from fastapi import APIRouter, Query
from app.controllers.user_weight_controller import user_weight_controller
from app.schemas import Success
from app.schemas.user_weight_schema import *

router = APIRouter()



@router.get("/getweightlist", summary="获取历史体重记录")
async def get_user_weights(user_id: str = Query(..., description="用户ID")):
    weights=await user_weight_controller.get_user_weights(user_id=user_id)
    return Success(data= [await weight.to_dict() for weight in weights])
