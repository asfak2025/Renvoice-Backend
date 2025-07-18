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


@router.delete("/delete/{districtId}")
async def delete_district_by_id(districtId: str):
    return await districts_controller.delete_district(districtId)


@router.get("/search")
async def search_districts(
    districtId: str = Query(None),
    name: str = Query(None)
):
    return await districts_controller.filter_districts(districtId, name)