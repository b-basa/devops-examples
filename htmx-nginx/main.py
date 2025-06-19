from fastapi import APIRouter, FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app_router = APIRouter(prefix="/api")

# Static files and templates setup
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Partial: Return a list of items (HTML snippet)
@app_router.get("/items")
async def get_items(request: Request):
    items = [{"name": "Item 1"}, {"name": "Item 2"}, {"name": "Item 3"}]
    return templates.TemplateResponse(
        "partials/items.html", {"request": request, "items": items}
    )


app.include_router(app_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
