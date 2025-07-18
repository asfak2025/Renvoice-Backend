# controllers/constituency_controller.py
from fastapi import HTTPException, status
from app.db.database import district_collection
from app.models.constituency_model import ConstituencyCreate, ConstituencyDB
from datetime import datetime

async def create_constituency(district_id: str, constituency: ConstituencyCreate):
    # 1. Check if district exists
    district = await district_collection.find_one({"district_id": district_id})
    if not district:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="District not found"
        )

    # 2. Check if constituency name already exists in this district (case-insensitive)
    existing_constituency = next(
        (c for c in district.get("constituency", []) 
        if c["constituency_name"].lower() == constituency.constituency_name.lower()),
        None
    )
    
    if existing_constituency:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Constituency with this name already exists in this district"
        )

    # 3. Create the full constituency object with ID
    constituency_db = ConstituencyDB(**constituency.dict())

    # 4. Update the district document
    result = await district_collection.update_one(
        {"district_id": district_id},
        {
            "$push": {"constituency": constituency_db.dict()},
            "$set": {"updatedAt": datetime.utcnow()}
        }
    )

    if result.modified_count == 0:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to add constituency to district"
        )

    return constituency_db


# controllers/constituency_controller.py

async def get_constituencies_by_district(district_id: str):
    
    # Find the district document
    district = await district_collection.find_one({"district_id": district_id})
    if not district:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="District not found"
        )
    
    if not district:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="District not found"
        )
    
    # Return the constituencies array or empty array if none exists
    return district.get("constituency", [])