from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI


from routing.product import router as product
from routing.orders import router as orders

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI(
    openapi_url="/core/openapi.json", docs_url="/docs"
)


app.include_router(product)
app.include_router(orders)


@app.get("/teleport")
async def get_teleport() -> RedirectResponse:
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

@app.get("/",
         description="tested",)
async def hello_world():
    return {"msg":"Hello World"}