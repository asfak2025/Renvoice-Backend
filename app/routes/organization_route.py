from fastapi import APIRouter
from app.controllers.organization_controller import create_organization
from app.models.organization_model import OrgCreateSchema, OrgResponseSchema

router = APIRouter()

@router.post("/createorg", response_model=OrgResponseSchema, tags=["Organization"])
async def create_org_route(data: OrgCreateSchema):
    return await create_organization(data)
