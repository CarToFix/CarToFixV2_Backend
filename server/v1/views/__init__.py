from fastapi import FastAPI, APIRouter

# Import routes
from .tasks import router as trouter
from .dashboard import router as drouter
from .clients import router as crouter
# HERE YOU IMPORT NEW ROUTERS


# Create the base router
base_router = APIRouter(prefix="/api/v1")

# Include imported routers in the base router
base_router.include_router(trouter)
base_router.include_router(drouter)
base_router.include_router(crouter)
# HERE YOU ADD NEW ROUTERS

# Create FastAPI app
app = FastAPI()

# Include the base router with the common prefix
app.include_router(base_router)
