from fastapi import APIRouter
from app.controllers import districts_controller
from app.models.districts import DistrictCreate
from fastapi import Query

router = APIRouter()

@router.post("/create")
async def create_district(district: DistrictCreate):
    return await districts_controller.create_district(district)



@router.get("/all")
async def get_all_districts():
    return await districts_controller.get_districts()


@router.delete("/delete/{district_id}")
async def delete_district_by_id(district_id: str):
    return await districts_controller.delete_district(district_id)


@router.get("/search")
async def search_districts(
    district_id: str = Query(None),
    name: str = Query(None)
):
    return await districts_controller.filter_districts(district_id, name)