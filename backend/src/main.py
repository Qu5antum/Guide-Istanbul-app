from fastapi import FastAPI
from backend.src.database.db import init_models
from fastapi.middleware.cors import CORSMiddleware
from backend.src.core.config.config import settings
import asyncio
import uvicorn
from backend.src.api.routers.user_router import router as user_router
from backend.src.api.routers.admin_panel_router import router as admin_panel
from backend.src.api.routers.locations_router import router as location_router
from backend.src.api.routers.reviews_router import router as review_router
from backend.src.api.routers.ai_assistant_router import router as ai_assistant_router

app = FastAPI(
    title = settings.app_name,
    debug=settings.debug,
    docs_url="/docs"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = settings.cors_origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(user_router)
app.include_router(location_router)
app.include_router(review_router)
app.include_router(ai_assistant_router)
app.include_router(admin_panel)

if __name__ == "__main__":
    asyncio.run(init_models())
    uvicorn.run(
        "backend.src.main:app", host="127.0.0.1", port=8000, reload=True
)



