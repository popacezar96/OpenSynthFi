from fastapi import FastAPI
from .api.routes import router
from .db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Random API Generator")
app.include_router(router)