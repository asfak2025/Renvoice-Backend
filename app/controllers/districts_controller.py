import time
import random
from app.db.database import district_collection
from app.models.districts import DistrictCreate
from fastapi import HTTPException
from datetime import datetime
from bson import ObjectId

# async def create_district(data: DistrictCreate):
#     try:
#         now_date = datetime.utcnow().isoformat()  
#         random_id = f"DIS{random.randint(1000, 9999)}" 

#         # Optional: Check for duplicate district name
#         existing = await district_collection.find_one({"name": data.name})
#         if existing:
#             raise HTTPException(status_code=400, detail="District already exists")

#         new_district = {
#             "districtId": random_id,
#             "name": data.name,
#             "createdAt": now_date,
#             "updatedAt": now_date,
#             "constituency": []
#         }

#         print("Creating District:", new_district)

#         result = await district_collection.insert_one(new_district)
#         if result.inserted_id:
#             return {
#                 "message": "District created successfully",
#                 "id": str(result.inserted_id)
#             }

#         raise HTTPException(status_code=500, detail="Failed to create district")
    
#     except Exception as e:
#         print("Error in create_district:", str(e))
#         raise HTTPException(status_code=500, detail=str(e))


async def create_district(data: DistrictCreate):
    try:
        # Check for duplicate
        existing = await district_collection.find_one({"name": data.name})
        if existing:
            raise HTTPException(status_code=400, detail="District already exists")

        # Generate unique districtId
        while True:
            random_id = f"DIS{random.randint(1000, 9999)}"
            id_check = await district_collection.find_one({"districtId": random_id})
            if not id_check:
                break

        now = datetime.utcnow()

        district_data = {
            "districtId": random_id,
            "name": data.name,
            "createdAt": now,
            "updatedAt": now,
            "constituency": []
        }

        result = await district_collection.insert_one(district_data)

        return {
            "message": "District created successfully",
            "id": str(result.inserted_id),
            "districtId": random_id
        }

    except Exception as e:
        print("❌ Error in create_district:", str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")

async def get_districts():
    try:
        cursor = district_collection.find({})
        districts = []
        async for district in cursor:
            district["_id"] = str(district["_id"])  
            districts.append(district)
        return {"districts": districts}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

async def delete_district(districtId: str):
    try:
        result = await district_collection.delete_one({"districtId": districtId})
        if result.deleted_count == 1:
            return {"message": f"District with ID {districtId} deleted successfully."}
        raise HTTPException(status_code=404, detail="District not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
async def filter_districts(districtId: str= None, name: str = None):
    try:
        query={}
        if districtId:
            query["districtId"]= districtId
        if name:
            query["name"] ={"$regex" : name, "$options" : "i"}

        cursor = district_collection.find(query)
        results = []
        async for doc in cursor:
            doc["_id"] = str(doc["_id"])
            results.append(doc)

        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
