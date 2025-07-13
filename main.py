from fastapi import FastAPI
from v1.api import router as v1_router
from core.settings import settings
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
)

app.include_router(v1_router, prefix="/v1")

if __name__ == "__main__":
    uvicorn.run(app)
