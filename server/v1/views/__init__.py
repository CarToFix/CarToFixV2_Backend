from fastapi import FastAPI, APIRouter

# Import routes
from .tasks import router as trouter
from .dashboard import router as drouter
from .clients import router as crouter
from .employees import route as erouter
from .parts import router as prouter
from .quotes import router as qrouter
from .specialisations import router as srouter
from .vehicle_brand import router as vbrouter
from .vehicle_model import router as vmrouter
from .vehicle_types import router as vtrouter
from .vehicles import router as vrouter
from .workshops import route as wrouter
from .tasks import router as trouter
# HERE YOU IMPORT NEW ROUTERS


# Create the base router
base_router = APIRouter(prefix="/api/v1")

# Include imported routers in the base router
base_router.include_router(trouter)
base_router.include_router(drouter)
base_router.include_router(crouter)
base_router.include_router(erouter)
base_router.include_router(prouter)
base_router.include_router(qrouter)
base_router.include_router(srouter)
base_router.include_router(vbrouter)
base_router.include_router(vmrouter)
base_router.include_router(vtrouter)
base_router.include_router(vrouter)
base_router.include_router(wrouter)
base_router.include_router(trouter)
# HERE YOU ADD NEW ROUTERS

# Create FastAPI app
app = FastAPI()

# Include the base router with the common prefix
app.include_router(base_router)
