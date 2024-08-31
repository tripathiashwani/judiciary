# models/meeting.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Meeting(BaseModel):
    meeting_id: str
    case_id: str
    title: str
    scheduled_at: datetime
    participants: List[str]  # List of user IDs (clients, lawyers, mediators)
    created_by: str  # User ID of the creator (usually a mediator)
    is_active: bool = True
    meeting_url: Optional[str] = None  # URL for video conferencing
