from fastapi import FastAPI
from app.routes import users

app = FastAPI(title="Clean Architecture API")

app.include_router(users.router, prefix="/users")
