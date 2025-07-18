from pydantic import BaseModel, HttpUrl, Field,ConfigDict
from datetime import datetime
from enum import Enum
from typing import Optional


class Status(str,Enum):
    active="active"
    inactive = "inactive"

class CampaignCreateSchema(BaseModel):
    campaignName:str
    campaignUrl:HttpUrl
    campaignDescription:str
    orgId:str
    status:Status = Status.active
    memberId:str




class CampaignResponseSchema(CampaignCreateSchema):
    campaignId:str

class GetAllCampaignsSchema(BaseModel):
    orgId:str
    memberId:str

class GetCampaignsResponse(GetAllCampaignsSchema):
    model_config = ConfigDict(extra='ignore')
    campaignName:str
    campaignId:str
    campaignDescription:str
    memberId:str
    orgId:str
    status:Status
    campaignUrl:HttpUrl

class GetAllCampaignsResponse(BaseModel):
    campaigns:list[GetCampaignsResponse]


class CampaignUpdate(BaseModel):
    campaignId:str
    
    status:Optional[Status] 


    