from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import user, case, meeting
from db import lifespan  # Import lifespan from db.py

# Initialize FastAPI app with lifespan management
app = FastAPI(lifespan=lifespan)

# CORS configuration
origins = ["http://localhost:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers for different modules
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(case.router, prefix="/cases", tags=["cases"])
app.include_router(meeting.router, prefix="/meetings", tags=["meetings"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
