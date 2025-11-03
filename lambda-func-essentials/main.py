from fastapi import FastAPI
from mangum import Mangum

from endpoints import router

app = FastAPI()

# Include routers
app.include_router(router=router)
