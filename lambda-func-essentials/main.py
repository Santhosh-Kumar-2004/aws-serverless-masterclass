from fastapi import FastAPI
from mangum import Mangum

from endpoints import router

app = FastAPI()

# Include routers
app.include_router(router=router)

# This is the entry point for AWS Lambda, with Mangum
handler = Mangum(app)