from typing import Annotated

from fastapi import FastAPI, Query
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()

@app.get("/")
async def index():
    return {"Hello": "World"}

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=20)] = None):
    results: dict[str, list[dict[str, str]] | str] = {
                "items":[{"item_id": "Foo"}, {"item_id": "Bar"}],
             }
    if q:
        results["q"] = q
    return results

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/")
async def create_item(item: Item):
    return item
