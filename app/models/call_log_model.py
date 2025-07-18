from pydantic import BaseModel, Field
from typing import Optional, Literal
from uuid import UUID
from datetime import datetime


class CallSummary(BaseModel):
    callDuration: int
    feedbackType: Optional[str] = None
    emotionalState: Optional[str] = None
    communicationPerfomance: Optional[str] = None


class CallLogCreate(BaseModel):
    type: Literal["incoming", "outgoing"]
    callStartTime: datetime
    callEndTime: datetime
    customerNumber: str
    agentNumber: str
    audioUrl: Optional[str] = None
    callStatus: Literal["pending", "active", "completed"]
    campaignId: str
    agentId: str
    callType: Literal["BOT", "HUMAN"]
    callEndBy: Literal["user", "agent"]
    callSummary: CallSummary


class CallLogDB(CallLogCreate):
    callId: UUID
    createdDate: str
