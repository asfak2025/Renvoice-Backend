from fastapi import APIRouter
from app.controllers.campaign_controller import creatCampaign
from app.models.campaign_model import CampaignResponseSchema,CampaignUpdate,CampaignCreateSchema,GetAllCampaignsSchema,GetAllCampaignsResponse
from app.controllers.campaign_controller import getAllCampaign , UpdateCampaign

router = APIRouter()

@router.post("/createCampaign",response_model=CampaignResponseSchema,tags=["campaign"])
async def create_campaign(data:CampaignCreateSchema):
    return await creatCampaign(data)

@router.post("/getCampaign",response_model=GetAllCampaignsResponse,tags=["campaign"])
async def get_campaigns(data:GetAllCampaignsSchema):
    return await getAllCampaign(data)

@router.post("/updateCampaign",tags=["campaign"])
async def Update_campaign(data:CampaignUpdate):
    return await UpdateCampaign(data)