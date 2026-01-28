from fastapi import FastAPI

from core.db import engine
from models import Base
from routers import auth, posts

app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(posts.router)
app.include_router(auth.router)
