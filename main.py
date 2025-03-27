from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from api_v1.products.views import router as router_v1
from core.config import settings
from core.models import db_helper, Base
from user.route import user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(user_router, tags=["Users"])
app.include_router(router=router_v1, prefix=settings.api_v1_prefix, tags=["Products"])

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
