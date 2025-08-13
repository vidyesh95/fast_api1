from fastapi import FastAPI
from typing import Optional, Any
from pydantic import BaseModel, EmailStr
from datetime import datetime

app = FastAPI()


# Define what a "User" looks like using a Pydantic model
class User(BaseModel):
    """
    Pydantic models are like strict templates for data
    They automatically validate and convert data types
    """
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    age: Optional[int] = None
    is_active: bool = True  # Default value


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/read-root")
def read_root():
    """
    This is a path operation function.
    It handles GET requests to the root path "/read-root"
    """
    return {"message": "Hello, World!"}


@app.get("/users/{user_id}")
def read_user(user_id: int):
    """
    {user_id} in the path becomes a parameter in your function
    The type hint 'int' tells FastAPI to ensure it's a number

    Try: /users/123 ✓ (works)
    Try: /users/abc ✗ (FastAPI returns an error - automatic validation!)
    """
    return {"user_id": user_id, "message": f"Getting info for user {user_id}"}


@app.get("/users/{user_id}/posts/{post_id}")
def read_user_post(user_id: int, post_id: int):
    """
    FastAPI extracts both parameters from the URL
    """
    return {
        "user_id": user_id,
        "post_id": post_id,
        "message": f"Post {post_id} from user {user_id}"
    }


@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10, search: Optional[str] = None):
    """
    Query parameters come after '?' in the URL
    Example: /items/?skip=20&limit=50&search=hammer

    - skip: where to start (default 0)
    - limit: how many to return (default 10)
    - search: optional search term (default None)

    Defaults make parameters optional - very convenient!
    """
    response: dict[str, Any] = {"skip": skip, "limit": limit}
    response = {"skip": skip, "limit": limit}
    if search:
        response["search"] = search
        response["message"] = f"Searching for items containing '{search}'"
    return response


@app.post("/users/")
def create_user(user: User):
    """
    FastAPI automatically:
    1. Reads the JSON from the request body
    2. Validates it matches the User model
    3. Converts it to a User object
    4. Gives you nice error messages if something's wrong
    """
    # You can access fields with dot notation
    message = f"Creating user {user.username} with email {user.email}"

    # You can convert to dictionary
    user_dict = user.model_dump()
    user_dict["created_at"] = datetime.now()

    return {"message": message, "user_data": user_dict}

