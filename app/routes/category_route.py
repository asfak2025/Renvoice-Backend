from fastapi import APIRouter, Query
from app.controllers import category_controller

router = APIRouter()

@router.get("/category/summary")
async def get_category_summary(
    districtId: str = Query(None),
    constituencyId: str = Query(None),
    categoryId: str = Query(None)
):
    return await category_controller.get_category_summary(
        districtId=districtId,
        constituencyId=constituencyId,
        category_id=categoryId
    )
