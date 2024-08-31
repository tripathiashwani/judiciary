# routers/user.py
from fastapi import APIRouter, HTTPException, Request
from models.user import UserCreate, UserResponse
from passlib.context import CryptContext
from bson import ObjectId

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register", response_model=UserResponse)
async def register_user(user: UserCreate, request: Request):
    """
    Register a new user.
    """
    user_collection = request.app.mongodb["users"]  # Access the users collection from the request object

    # Check if the email is already registered
    existing_user = await user_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the user's password
    hashed_password = pwd_context.hash(user.password)
    user_data = {
        "username": user.username,
        "email": user.email,
        "role": user.role,
        "hashed_password": hashed_password
    }

    # Insert new user data into the database
    result = await user_collection.insert_one(user_data)
    user_data["_id"] = str(result.inserted_id)

    # Return the user response model
    return UserResponse(id=user_data["_id"], **user.model_dump())
