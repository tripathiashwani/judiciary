# routers/case.py
from fastapi import APIRouter, HTTPException, Request
from models.case import Case
from bson import ObjectId
from enum import Enum

router = APIRouter()

@router.post("/", response_model=Case)
async def create_case(case: Case, request: Request):
    """
    Create a new case.
    """
    case_data = case.model_dump()  # Use model_dump to convert model to dictionary
    # Access the case collection from the request object
    case_collection = request.app.mongodb["cases"]
    result = await case_collection.insert_one(case_data)
    case_data["_id"] = str(result.inserted_id)
    return Case(**case_data)

@router.get("/{case_id}", response_model=Case)
async def get_case(case_id: str, request: Request):
    """
    Retrieve a case by its ID.
    """
    # Access the case collection from the request object
    case_collection = request.app.mongodb["cases"]
    case_data = await case_collection.find_one({"_id": ObjectId(case_id)})
    if case_data:
        case_data["_id"] = str(case_data["_id"])
        return Case(**case_data)
    raise HTTPException(status_code=404, detail="Case not found")
