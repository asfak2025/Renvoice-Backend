from pydantic import BaseModel, HttpUrl, Field
from typing import List, Optional
import uuid


class OrgCreateSchema(BaseModel):
    orgName: str = Field(..., min_length=1)
    orgStatus: str 
    orgLogo: HttpUrl 
    orgMembers: List[dict] = []
    orgAgent: List[dict] = []
    orgSupportAccess: List[dict] = []
    orgAdminAccess: List[dict] = []
    orgCollectionAccess: List[dict] = []


class OrgResponseSchema(OrgCreateSchema):
    orgId: str
