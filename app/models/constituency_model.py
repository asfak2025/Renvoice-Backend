from pydantic import BaseModel, Field
from typing import List
from app.utils.generate import generate_uuid, generate_epoch_id

class MemberSchema(BaseModel):
    member_id: str = Field(default_factory=generate_uuid)
    member_name: str
    member_position: str

# Request schema
class ConstituencyCreate(BaseModel):
    constituency_name: str
    constituency_members: List[MemberSchema] = []

# DB + Response schema
class ConstituencyDB(ConstituencyCreate):
    constituency_id: str = Field(default_factory=lambda: generate_epoch_id("CN_"))
