import uuid
from fastapi import HTTPException
from app.db.database import client
from app.models.organization_model import OrgCreateSchema, OrgResponseSchema

org_collection = client.db.org_collection

async def create_organization(data: OrgCreateSchema) -> OrgResponseSchema:
    # Check if org with same name exists
    existing = await org_collection.find_one({"orgName": data.orgName})
    if existing:
        raise HTTPException(status_code=400, detail="Organization already exists.")

    # Prepare the new org document
    new_org = data.dict()
    new_org["orgId"] = str(uuid.uuid4())

    # Insert into DB
    result = await org_collection.insert_one(new_org)
    if not result.inserted_id:
        raise HTTPException(status_code=500, detail="Failed to create organization")

    return OrgResponseSchema(**new_org)
