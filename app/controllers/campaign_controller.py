import uuid
from fastapi import HTTPException
from app.db.database import campaign_collection
from app.utils.generate import generate_epoch_id
from app.models.campaign_model import CampaignCreateSchema, CampaignResponseSchema, CampaignUpdate
from app.models.campaign_model import GetAllCampaignsSchema, GetCampaignsResponse, GetAllCampaignsResponse





async def creatCampaign(data=CampaignCreateSchema) ->CampaignResponseSchema:
    new_campaign = data.model_dump(mode="json")
    new_campaign["campaignId"] = generate_epoch_id("CPN")

    result = await campaign_collection.insert_one(new_campaign)
    if not result.inserted_id:
        raise HTTPException(status_code=500, detail="Failed to create Campaign")

    return CampaignResponseSchema(**new_campaign)

async def getAllCampaign(data = GetAllCampaignsSchema) ->GetAllCampaignsResponse:
    
    campaigns =  campaign_collection.find({"orgId":data.orgId,"memberId":data.memberId},projection={"_id":0})
    result = await campaigns.to_list(length=100)
    print("result",result)
    if not result:
        raise HTTPException(status_code=404,detail="Not Found")
    return GetAllCampaignsResponse(campaigns=result) 

async def UpdateCampaign(data = CampaignUpdate):
    if not data.campaignId:
        raise HTTPException(status=400,detail="Campaign Id required")
    result = await campaign_collection.update_one({"campaignId":data.campaignId},{"$set":{"status":data.status}})
    if result.matched_count ==0:
        raise HTTPException(status_code=404,detail="Campain Not Found")
    return "Updated"
    