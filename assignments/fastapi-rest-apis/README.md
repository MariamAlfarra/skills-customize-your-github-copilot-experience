# 🛠 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using the FastAPI framework. Learn how to define endpoints, use request data, and return JSON responses.

## 📝 Tasks

### 🛠️ Task 1: Set up the FastAPI application

#### Description
Create a new FastAPI app and add a root endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Create a FastAPI application instance
- Define a GET endpoint at `/` that returns a JSON response
- Use `uvicorn` or a similar server to run the app locally

### 🛠️ Task 2: Add API endpoints for items

#### Description
Create additional endpoints for reading and creating items using Pydantic models.

#### Requirements
Completed program should:

- Define a Pydantic `Item` model with fields for `id`, `name`, `description`, and `price`
- Add a GET endpoint at `/items/{item_id}` that returns the matching item or an error if not found
- Add a POST endpoint at `/items` that accepts item data and returns a success response
- Keep item records in a simple in-memory list for this assignment
