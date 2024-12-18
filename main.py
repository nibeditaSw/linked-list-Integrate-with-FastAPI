from fastapi import FastAPI
from linked_list import LinkedList

app = FastAPI()
linked_list = LinkedList()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Linked List API!"}


@app.get("/get-data/")
def get_data():
    """Retrieve all data from the linked list."""
    data = linked_list.get_data()
    return {"linked_list": data}


@app.post("/add-at-beginning/")
def add_at_beginning(data: str):
    """Add a node at the beginning of the linked list."""
    message = linked_list.add_at_beginning(data)
    return {"message": message}


@app.post("/add-at-end/")
def add_at_end(data: str):
    """Add a node at the end of the linked list."""
    message = linked_list.add_at_end(data)
    return {"message": message}

@app.put("/update-node/")
def update_node(old_data: str, new_data: str):
    """Update a node's value in the linked list."""
    message = linked_list.update_node(old_data, new_data)
    return {"message": message}


@app.delete("/delete-node/")
def delete_node(data: str):
    """Delete a node from the linked list."""
    message = linked_list.delete_node(data)
    return {"message": message}
