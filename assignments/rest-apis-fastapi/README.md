# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build scalable and modern REST APIs using FastAPI, a high-performance Python framework. You'll create endpoints to retrieve and manage data, understanding HTTP methods, request/response handling, and how APIs power modern applications.

## 📝 Tasks

### 🛠️ Set Up a FastAPI Application and Create GET Endpoints

#### Description
Initialize a FastAPI application and create your first endpoints that retrieve data. You'll understand how FastAPI automatically generates documentation and handles HTTP GET requests.

#### Requirements
Completed program should:

- Import and instantiate a FastAPI application
- Create a GET endpoint at `/` that returns a welcome message (as JSON)
- Create a GET endpoint at `/items/` that returns a list of sample items (with id and name)
- Run the server using `uvicorn` and verify endpoints respond correctly

### 🛠️ Implement POST Endpoints to Create Resources

#### Description
Add the ability for clients to send data to your API and create new resources. You'll implement POST endpoints and handle request bodies with data models.

#### Requirements
Completed program should:

- Create a data model for items using Pydantic (with fields like id, name, and description)
- Create a POST endpoint at `/items/` that accepts JSON input and adds it to your data storage
- Maintain an in-memory list of items (the created item should persist during the session)
- Return the created item with its assigned id and a 200 status code

### 🛠️ Add Path and Query Parameters

#### Description
Make your API more flexible by supporting dynamic data requests through path parameters (for specific items) and query parameters (for filtering). This is crucial for building practical APIs.

#### Requirements
Completed program should:

- Create a GET endpoint at `/items/{item_id}/` that retrieves a specific item by id
- Add a query parameter `skip` to `/items/?skip=0` to paginate results (e.g., return items starting from index `skip`)
- Return appropriate error responses (e.g., 404) when an item is not found
- Document the purpose of each parameter so clients understand your API
