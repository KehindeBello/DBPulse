from fastapi import APIRouter, BackgroundTasks, Request
from models.models import MonitorPayload
from core.monitor import server_status

router = APIRouter()

@router.post("/tick", status_code=202)
async def monitor(request: Request, background_tasks: BackgroundTasks):
    payload: MonitorPayload = await request.json()
    background_tasks.add_task(server_status, payload)
    return {"status": "accepted"}
