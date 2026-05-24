from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

# Crear instancia de FastAPI
app = FastAPI(
    title="Finance Tracker API",
    description="Personal Finance Management System API",
    version="1.0.0",
    debug=settings.DEBUG
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """
    Endpoint raíz de la API
    """
    return {
        "message": "Finance Tracker API",
        "version": "1.0.0",
        "status": "running",
        "environment": settings.ENVIRONMENT,
        "docs_url": "/docs"
    }


@app.get("/health")
async def health_check():
    """
    Health check endpoint para verificar que la API está funcionando
    """
    return {
        "status": "healthy",
        "environment": settings.ENVIRONMENT
    }