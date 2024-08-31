from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI
from contextlib import asynccontextmanager

# MongoDB connection details
MONGO_DETAILS = "mongodb://localhost:27017"  # Use the local MongoDB server or update with the correct URI

# Initialize MongoDB client
client = AsyncIOMotorClient(MONGO_DETAILS)
db = client["mediation_platform"]  # Define your database name

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Connect to MongoDB at startup
    await startup_db_client(app)
    yield
    # Disconnect from MongoDB at shutdown
    await shutdown_db_client(app)

async def startup_db_client(app):
    # Setup the MongoDB client connection
    app.mongodb_client = AsyncIOMotorClient(
        "mongodb+srv://tashwani475:xUxu6t39TjQpRLYH@cluster0.wt0qf.mongodb.net/"  # Update this if you use a different MongoDB server
    )
    app.mongodb = app.mongodb_client.get_database("mediation_platform")
    print("MongoDB connected.")

async def shutdown_db_client(app):
    # Close the MongoDB client connection
    app.mongodb_client.close()
    print("Database disconnected.")

# Initialize FastAPI app with lifespan
app = FastAPI(lifespan=lifespan)
