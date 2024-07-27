from fastapi import FastAPI

app = FastAPI()

# Minimal app - GET request


@app.get("/", tags=["root"])
async def root() -> dict:
    return {"message": "Welcome to this fantastic app!"}

# GET --> Read Todo


@app.get("/todo", tags=["todos"])
async def get_todo() -> dict:
    return {"data": todos}


# POST --> Create Todo
@app.post("/todo", tags=["todos"])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {"data": "Todo added successfully."}

# PUT --> Update Todo


@app.put("/todo/{id}", tags=["todos"])
async def update_todo(id: int, todo: dict) -> dict:
    for i in range(len(todos)):
        if todos[i]["id"] == id:
            todos[i] = todo
            return {"data": f"Todo with id {id} has been updated successfully."}
    return {"data": f"Todo with id {id} not found."}

# DELETE --> Delete Todo


@app.delete("/todo/{id}", tags=["todos"])
async def delete_todo(id: int) -> dict:
    for i in range(len(todos)):
        if todos[i]["id"] == id:
            todos.pop(i)
            return {"data": f"Todo with id {id} has been deleted successfully."}
    return {"data": f"Todo with id {id} not found."}

# List of todos
todos: list[dict] = [
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
