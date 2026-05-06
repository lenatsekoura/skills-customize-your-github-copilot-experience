"""
Starter code for Building REST APIs with FastAPI assignment.

This template provides the basic structure for a FastAPI application.
Complete the tasks by filling in the endpoints and adding the necessary functionality.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize the FastAPI application
app = FastAPI(title="Item API", description="A simple REST API for managing items")

# Define the Item data model using Pydantic
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

# In-memory storage for items (replace with a database in production)
items_db: List[Item] = []
next_item_id = 1


# Task 1: Create GET endpoints
@app.get("/")
def read_root():
    """
    Welcome endpoint that returns a greeting message.
    TODO: Return a dictionary with a welcome message.
    """
    pass


@app.get("/items/")
def read_items(skip: int = 0):
    """
    Retrieve all items with optional pagination using the skip parameter.
    TODO: Return items starting from the skip index.
    """
    pass


# Task 2: Implement POST endpoint
@app.post("/items/")
def create_item(item: Item):
    """
    Create a new item and add it to the database.
    TODO: Assign an id, store the item, and return it.
    """
    pass


# Task 3: Add path and query parameters
@app.get("/items/{item_id}/")
def read_item(item_id: int):
    """
    Retrieve a specific item by its id.
    TODO: Return the item if found, otherwise raise a 404 error.
    """
    pass


# Run the app with: uvicorn starter-code:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
