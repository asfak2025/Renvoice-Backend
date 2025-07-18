from pydantic import BaseModel
from typing import List


class DistrictCreate(BaseModel):
    name: str


class DistrictDB(DistrictCreate):
    district_id: str
    createdAt: int
    updatedAt: int
    constituency: List = []
