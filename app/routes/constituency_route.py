# routes/constituency_routes.py
from fastapi import APIRouter, Path
from app.models.constituency_model import ConstituencyCreate, ConstituencyDB
from app.controllers.constituency_controller import create_constituency, get_constituencies_by_district
from typing import List
from fastapi import APIRouter, Path, HTTPException, status

router = APIRouter()

@router.post("/{district_id}/constituencies", 
            response_model=ConstituencyDB,
            tags=["Constituency"])
async def create_constituency_route(
    constituency: ConstituencyCreate,
    district_id: str = Path(..., description="The ID of the district to add the constituency to")
):
    return await create_constituency(district_id, constituency)

# routes/constituency_routes.py

@router.get("/{district_id}/constituencies", 
           response_model=List[ConstituencyDB],
           tags=["Constituency"])
async def get_constituencies_route(
    district_id: str = Path(..., description="The ID of the district to get constituencies from")
):
    return await get_constituencies_by_district(district_id)