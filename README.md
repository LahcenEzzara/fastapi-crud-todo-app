![FastAPI Logo](https://raw.githubusercontent.com/LahcenEzzara/fastapi-getting-started/main/fastapi.png)

---

# FastAPI Todo CRUD App

This is a simple Todo CRUD (Create, Read, Update, Delete) application built with FastAPI. The app allows you to manage a list of todos with various activities throughout the day.

## Repository Name

`fastapi-crud-todo-app`

## Features

- **Create Todo**: Add new todos to the list.
- **Read Todo**: Retrieve the list of all todos.
- **Update Todo**: Modify existing todos by ID.
- **Delete Todo**: Remove todos by ID.

## Getting Started

### Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/LahcenEzzara/fastapi-crud-todo-app.git
   cd fastapi-crud-todo-app
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install fastapi
   ```

### Running the App

1. Start the FastAPI server:

   ```bash
   fastapi dev
   ```

2. Open your browser and navigate to `http://127.0.0.1:8000` to see the welcome message.

3. To interact with the Todo API, go to `http://127.0.0.1:8000/docs` for the interactive Swagger UI.

## API Endpoints

- **Root Endpoint**

  ```http
  GET /
  ```

  Returns a welcome message.

- **Get Todos**

  ```http
  GET /todo
  ```

  Retrieves the list of all todos.

- **Add Todo**

  ```http
  POST /todo
  ```

  Adds a new todo. Expects a JSON body with the todo details.

- **Update Todo**

  ```http
  PUT /todo/{id}
  ```

  Updates an existing todo by ID. Expects a JSON body with the updated todo details.

- **Delete Todo**

  ```http
  DELETE /todo/{id}
  ```

  Deletes a todo by ID.

## Example Todo List

Here's an example of a todo list included in the app:

```json
[
    {
        "id": 1,
        "Activity": "Wake up and freshen up at 6:00 AM."
    },
    {
        "id": 2,
        "Activity": "Jogging for 2 hours at 7:00 AM."
    },
    {
        "id": 3,
        "Activity": "Have breakfast at 9:00 AM."
    },
    {
        "id": 4,
        "Activity": "Attend AI and computer engineering class at 10:00 AM."
    },
    {
        "id": 5,
        "Activity": "Study and complete assignments at 12:00 PM."
    },
    {
        "id": 6,
        "Activity": "Have lunch at 1:00 PM."
    },
    {
        "id": 7,
        "Activity": "Writing 3 pages of my new book at 2:00 PM."
    },
    {
        "id": 8,
        "Activity": "Take a short nap at 4:00 PM."
    },
    {
        "id": 9,
        "Activity": "Go to the gym at 5:00 PM."
    },
    {
        "id": 10,
        "Activity": "Return home and shower at 7:00 PM."
    },
    {
        "id": 11,
        "Activity": "Prepare and have dinner at 8:00 PM."
    },
    {
        "id": 12,
        "Activity": "Relax and watch TV or read a book at 9:00 PM."
    },
    {
        "id": 13,
        "Activity": "Work on personal projects or hobbies at 10:00 PM."
    },
    {
        "id": 14,
        "Activity": "Prepare for bed and unwind at 11:00 PM."
    },
    {
        "id": 15,
        "Activity": "Go to sleep at 11:30 PM."
    }
]
```

## Copyrights

This project is licensed under the MIT License. See the LICENSE file for more details.

**© 2024 Lahcen Ezzara**
```
