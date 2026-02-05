from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import auth, users
from app.db.mysql import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Clean Architecture",
    description="Professional FastAPI project with JWT auth, MySQL, MongoDB and clean architecture",
    version="1.0.0",
)

# CORS (ajuste se expor frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")


@app.get("/health", tags=["health"])
def health_check():
    """
    Health check endpoint.
    Used for monitoring, Docker and Kubernetes probes.
    """
    return {"status": "ok"}
