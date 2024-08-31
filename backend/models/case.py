# models/case.py
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from enum import Enum


class CaseStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"

class Case(BaseModel):
    case_id: str
    title: str
    description: Optional[str] = None
    status: CaseStatus
    client_id: str
    lawyer_ids: List[str]
    mediator_id: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    documents: Optional[List[str]] = []  # List of document URLs
    next_meeting: Optional[datetime] = None
