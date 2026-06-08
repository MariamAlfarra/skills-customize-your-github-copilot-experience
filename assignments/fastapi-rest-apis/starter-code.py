from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

items: List[dict] = [
    {"id": 1, "name": "Pen", "description": "A blue ink pen", "price": 1.50},
    {"id": 2, "name": "Notebook", "description": "A lined notebook", "price": 3.99},
]

@app.get("/")
async def read_root():
    """Return a welcome message from the API."""
    return {"message": "Welcome to the FastAPI assignment!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """Return the item for the requested ID or raise a 404 error."""
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items")
async def create_item(item: Item):
    """Create a new item from the request body."""
    items.append(item.dict())
    return {"message": "Item created", "item": item}
