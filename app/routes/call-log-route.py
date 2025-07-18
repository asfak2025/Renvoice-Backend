from fastapi import APIRouter, Request
from app.controllers.call_log_controler import create_call_log
from app.models.call_log_model import CallLogCreate

router = APIRouter()


@router.post("/call-logs", tags=["Call Logs"])
async def create_log(request: Request, call_log: CallLogCreate):
    return await create_call_log(call_log)
