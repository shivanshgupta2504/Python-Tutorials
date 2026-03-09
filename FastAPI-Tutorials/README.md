# FastAPI Tutorials

This repository contains tutorials and examples for learning FastAPI. 

Before diving into the code, let's understand some prerequisite concepts to build a strong foundation.

## Pre-requisite Concepts

### 1. Web
The Web (World Wide Web) is a massive collection of interconnected documents and resources, linked by hyperlinks and URLs. It operates over the Internet, allowing clients (like your web browser) to request and receive information from servers.

### 2. HTTP (HyperText Transfer Protocol)
HTTP is the foundation of data communication for the World Wide Web. It's a protocol (a set of rules) that defines how messages are formatted and transmitted, and what actions web servers and browsers should take in response to various commands.
- **Methods/Verbs:** `GET` (retrieve data), `POST` (send submit data), `PUT` (update data), `DELETE` (remove data), etc.
- **Status Codes:** `200 OK` (success), `404 Not Found` (resource doesn't exist), `500 Server Error`, etc.

### 3. APIs (Application Programming Interfaces)
An API is a set of rules and protocols that allows one software application to interact with another. It acts as an intermediary, enabling different systems to communicate. For example, a weather app on your phone uses an API to get data from a weather service's database.

### 4. RESTful APIs
REST (Representational State Transfer) is an architectural style for designing networked applications. A RESTful API relies on standard HTTP methods and conventions.
- It uses standard HTTP actions (`GET`, `POST`, `PUT`, `DELETE`) to perform operations on resources (like a "User" or a "Post").
- It is stateless: each request from client to server must contain all the information needed to understand the request.

### 5. ASGI (Asynchronous Server Gateway Interface)
ASGI is a spiritual successor to WSGI, designed to provide a standard interface between async-capable Python web servers, frameworks, and applications. FastAPI is an asynchronous framework, which means it uses ASGI to handle many concurrent connections smoothly and efficiently. (Uvicorn is a popular ASGI server used to run FastAPI apps).

### 6. URL and its Parts
A URL (Uniform Resource Locator) is the address of a given unique resource on the Web.
Example: `https://www.example.com:8080/path/to/resource?query1=value1#section`
- **Protocol/Scheme (`https://`):** Tells the browser how to connect (e.g., HTTP vs HTTPS).
- **Domain (`www.example.com`):** The human-readable name of the server computer.
- **Port (`:8080`):** (Optional) The specific "door" to enter on the server. Defaults to 80 for HTTP and 443 for HTTPS.
- **Path (`/path/to/resource`):** The location of the specific resource on the server.
- **Query Parameters (`?query1=value1`):** (Optional) Extra data sent to the server to filter or modify the request.
- **Fragment (`#section`):** (Optional) Points to a specific location within the page.

### 7. How Data Flows Through the Web
1. **Client Request:** You type a URL in your browser or an app makes an API call. The client sends an HTTP Request to the server.
2. **DNS Resolution:** (If a domain is used) The domain name is translated into an IP address.
3. **Server Processing:** The web server receives the request, processes the path and data, and typically hands it off to your web framework (like FastAPI).
4. **App Logic:** Your FastAPI code runs, interacts with a database if necessary, and prepares a response.
5. **Server Response:** The server sends back an HTTP Response containing a status code and the requested data (often in JSON format for APIs, or HTML for websites).
6. **Client Rendering/Handling:** The client receives the response and displays the webpage or processes the API data.

---

## FastAPI Concepts (Related to `Tut-1`)

The folder `Tut-1` contains a basic introduction to setting up a FastAPI app. Here are the core FastAPI concepts demonstrated in that code.

### 1. Creating a FastAPI Instance
```python
from fastapi import FastAPI
app = FastAPI()
```
- `FastAPI()` is a Python class that provides all the functionality for your API.
- The `app` variable is the instance of this class. It acts as the main point of interaction to create all your API pathways. This is what the ASGI server (like Uvicorn) uses to run the application.

### 2. Path Operations (Routes)
A "path" (or route) is the part of the URL after the main domain (e.g., `/` or `/api/posts`).
An "operation" refers to one of the HTTP methods (e.g., GET, POST).
```python
@app.get("/")
def home():
    return {"message": "Hello World"}
```
- **The Decorator (`@app.get("/")`):** This is a "path operation decorator". It tells FastAPI that the function right below it is in charge of handling requests that go to:
  - the path `/`
  - using an HTTP `GET` operation
- **The Path Operation Function (`def home():`):** This is the normal Python function that gets called whenever FastAPI receives a request matching the decorator.

### 3. Returning Data Types
In FastAPI, you can return standard Python data types directly from your path operation functions:
- `dict`, `list`, `str`, `int`, etc.
FastAPI automatically converts these into JSON (JavaScript Object Notation), which is the standard format for web APIs.
In `Tut-1/main.py`, returning a list of dictionaries (`return posts`) is automatically serialized into a JSON array of objects.

### 4. Custom Responses (`HTMLResponse`)
By default, FastAPI assumes you want to return JSON. However, you can return other types of responses, such as plain HTML.
```python
from fastapi.responses import HTMLResponse

@app.get("/html_response", response_class=HTMLResponse)
def html_response():
    return f"<h1>{posts[0]['title']}</h1>"
```
- We import `HTMLResponse` from `fastapi.responses`.
- We use the `response_class` parameter in the decorator to tell FastAPI that this endpoint returns HTML, not JSON. The browser will render this as a webpage.

### 5. Decorator Parameters
FastAPI decorators can take extra parameters to modify behavior.
- `include_in_schema=False`: This prevents the endpoint from showing up in the auto-generated API documentation (Swagger UI at `/docs`).

### 6. Multiple Routes for the Same Function
You can stack multiple decorators on top of a single function. This allows multiple different URLs to trigger the exact same code and return the same result.
```python
@app.get("/html_response", response_class=HTMLResponse, include_in_schema=False)
@app.get("/html_response_copy", response_class=HTMLResponse, include_in_schema=False)
def html_response():
    return f"<h1>{posts[0]['title']}</h1>"
```
Both `/html_response` and `/html_response_copy` will hit this logic.
