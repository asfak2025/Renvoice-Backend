from uuid import uuid4
from app.db.database import call_collection
from app.models.call_log_model import CallLogCreate, CallLogDB
from app.utils.generate import generate_indian_date,generate_uuid
from fastapi import HTTPException
from datetime import datetime


async def create_call_log(data: CallLogCreate):
    new_log = {
        "callId": generate_uuid(),
        "type": data.type,
        "createdDate": generate_indian_date(),
        "callStartTime": data.callStartTime,
        "callEndTime": data.callEndTime,
        "customerNumber": data.customerNumber,
        "agentNumber": data.agentNumber,
        "audioUrl": data.audioUrl,
        "callStatus": data.callStatus,
        "campaignId": data.campaignId,
        "agentId": data.agentId,
        "callType": data.callType,
        "callEndBy": data.callEndBy,
        "callSummary": data.callSummary.dict()
    }

    result = await call_collection.insert_one(new_log)
    if result.inserted_id:
        return {"message": "Call log created successfully", "id": str(result.inserted_id)}
    raise HTTPException(status_code=500, detail="Failed to create call log")
