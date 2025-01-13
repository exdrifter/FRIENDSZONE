## FRIENDSZONE: API Documentation

### A. Overview
FRIENDSZONE allows users to manage blog posts, including creating, reading, updating, and deleting posts. This API provides CRUD operations on blog posts, such as creating, reading, updating, and deleting them. The API is intended to simplify communication between a front-end application and a backend server, allowing users to effectively manage their blog content.

### B. Endpoint Descriptions
#### 1. CREATE New Blog Post
- URL: ```/api/add```
- HTTP Method: POST
- Required Parameters:

Body:
```
{
  "title": "string",
  "date": "date",
  "content": "string",
}
```
Example Request:
```
{
  "btitle": "First Blog Test",
  "bdate": "(input date)",
  "bcontent": "Testing: Contents ahead.",
  }
```
Example Response:
```
{
  "id": 1,
  "btitle": "First Blog Test",
  "bcontent": "Testing: Contents ahead.",
  "bdate": "2025-01-13"
}
```
#### 2. GET All Blog Post
- URL: ```/api/blogs```
- HTTP Method: GET
- Required Parameters: None

Example Response:
```
[
  {
    "id": 1,
    "btitle": First Blog Test",
    "bcontent": "Testing: Contents Ahead",
    "bdate": "2025-01-13"
  },
  {
    "id": 2,
    "btitle": "my daily mantra",
    "bcontent": "i miss you zeussssssssssssssssssssssssssss ????!!!?!?!",
     "bdate": "2025-01-13"
  }
]
```
#### 3.UPDATE A Blog Post
- URL: ```/api/edit/{id}```
- HTTP Method: PUT
- Required Parameters:
  
Path:

    id: integer (blog post ID)

Body:
```
{
"title": "string",
"content": "string",
"date": "date"
}
```
#### 4. DELETE A Blog Post
- URL: ```/api/blogs/{id}```
- HTTP Method: DELETE
- Required Parameters:
  
Path:

    id: integer (blog post ID)

Example Request:
```
{
            "id": 1
}
```
Example Response:
```
{
        "message": "Post deleted."
}
```
### C.Error Handling
The API uses standard HTTP status codes to indicate the success or failure of requests. Here are some possible errors:
- 400 Bad Request:
```
{
            "error": "Invalid request parameters."
}
```
- 404 Not Found:
```
{
            "error": "Blog post not found."
}
```
- 500 Internal Server Error:
```
{
            "error": "An unexpected error occurred."
}
```



