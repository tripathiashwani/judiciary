# routers/meeting.py
from fastapi import APIRouter, HTTPException, Request, Depends
from models.meeting import Meeting
from bson import ObjectId

router = APIRouter()

@router.post("/", response_model=Meeting)
async def schedule_meeting(meeting: Meeting, request: Request):
    """
    Schedule a new meeting.
    """
    meeting_data = meeting.model_dump()  # Use model_dump instead of dict
    # Access the meeting collection from the request object
    meeting_collection = request.app.mongodb["meetings"]
    result = await meeting_collection.insert_one(meeting_data)
    meeting_data["_id"] = str(result.inserted_id)
    return Meeting(**meeting_data)

@router.get("/{meeting_id}", response_model=Meeting)
async def get_meeting(meeting_id: str, request: Request):
    """
    Retrieve a meeting by its ID.
    """
    # Access the meeting collection from the request object
    meeting_collection = request.app.mongodb["meetings"]
    meeting_data = await meeting_collection.find_one({"_id": ObjectId(meeting_id)})
    if meeting_data:
        meeting_data["_id"] = str(meeting_data["_id"])
        return Meeting(**meeting_data)
    raise HTTPException(status_code=404, detail="Meeting not found")
