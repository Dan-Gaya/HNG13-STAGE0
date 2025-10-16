from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes_profile import router as profile_router
import logging
import uvicorn


import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Initialize app
app = FastAPI(title="Profile API with MVC Architecture", version="1.0.0")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(profile_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Profile API"}

# Log the running URL once the app starts
@app.on_event("startup")
async def startup_event():
    logger.info("🚀 FastAPI is running at: http://127.0.0.1:8000")
    logger.info("📘 Docs available at: http://127.0.0.1:8000/docs")
    logger.info("🔗 Profile endpoint: http://127.0.0.1:8000/me")

# Only run with `python main.py`
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
