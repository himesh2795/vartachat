from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1.health import router as health_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="A FastAPI-based chat application",
    version="0.1.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(
    health_router,
    prefix=settings.API_V1_STR,
    tags=["health"]
)

@app.get("/")
async def root():
    """Root endpoint that provides API information."""
    return {
        "message": "Welcome to the Chat API",
        "docs": "/docs",
        "redoc": "/redoc"
    }

def main():
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    main()
