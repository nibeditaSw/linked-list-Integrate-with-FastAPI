from logging import *
from fastapi import FastAPI, HTTPException, Query
from linked_list import LinkedList

# Configure logging
basicConfig(
    # filename="linked_list.log",
    # filemode="a",
    format="{asctime} | {levelname} | {message}",
    datefmt="%d-%b-%y %H:%M:%S",
    level=10,
    style="{"
)

app = FastAPI()
linked_list = LinkedList()


def log_and_raise_exception(message: str):
    """Log an exception and raise HTTPException."""
    exception(message)
    raise HTTPException(status_code=400, detail=message)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Linked List API!"}


@app.get("/get-data/")
def get_data():
    """Retrieve all data from the linked list."""
    data = linked_list.get_data()
    return {"linked_list": data}


@app.post("/add-at-beginning/")
def add_at_beginning(data: str = Query(None)):
    """
    Add a node at the beginning of the linked list.
    Parameters:
        data (str): Data for the new node.
    """
    if data is None:
        log_and_raise_exception("Data is null. Cannot add node at the beginning.")
    message = linked_list.add_at_beginning(data)
    return {"message": message}


@app.post("/add-at-end/")
def add_at_end(data: str = Query(None)):
    """
    Add a node at the end of the linked list.
    Parameters:
        data (str): Data for the new node.
    """
    if data is None:
        log_and_raise_exception("Data is null. Cannot add node at the end.")
    message = linked_list.add_at_end(data)
    return {"message": message}


@app.put("/update-node/")
def update_node(old_data: str = Query(None), new_data: str = Query(None)):
    """
    Update a node's value in the linked list.
    Parameters:
        old_data (str): The current value to update.
        new_data (str): The new value to set.
    """
    if old_data is None or new_data is None:
        log_and_raise_exception("Old data or new data is null. Cannot update node.")
    message = linked_list.update_node(old_data, new_data)
    return {"message": message}


@app.delete("/delete-node/")
def delete_node(data: str = Query(None)):
    """
    Delete a node from the linked list.
    Parameters:
        data (str): The value of the node to delete.
    """
    if data is None:
        log_and_raise_exception("Data is null. Cannot delete node.")
    message = linked_list.delete_node(data)
    return {"message": message}
