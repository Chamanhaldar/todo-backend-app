from fastapi import FastAPI
from .config import settings
from .database import engine, Base
from .routers import todos


app = FastAPI(title="Todo API")


# Create DB tables (for dev/demo only — use migrations in prod)
Base.metadata.create_all(bind=engine)


app.include_router(todos.router, prefix=settings.API_V1_STR)


@app.get("/health")
def health():
  return {"status": "ok"}