from fastapi import FastAPI, APIRouter

# Routes
from .dashboard import router as drouter

# Create the base router
base_router = APIRouter(prefix="/api/v1")

# Include the dashboard router in the base router
base_router.include_router(drouter)

# Create FastAPI app
app = FastAPI()

# Include the base router with the common prefix
app.include_router(base_router)
