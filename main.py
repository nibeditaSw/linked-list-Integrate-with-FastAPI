# from logging import *
# from fastapi import FastAPI, HTTPException, Query
# from linked_list import LinkedList

# # Configure logging
# basicConfig(
#     # filename="linked_list.log",
#     # filemode="a",
#     format="{asctime} | {levelname} | {message}",
#     datefmt="%d-%b-%y %H:%M:%S",
#     level=10,
#     style="{"
# )

# app = FastAPI()
# linked_list = LinkedList()


# def log_and_raise_exception(message: str):
#     """Log an exception and raise HTTPException."""
#     exception(message)
#     raise HTTPException(status_code=400, detail=message)


# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Linked List API!"}


# @app.get("/get-data/")
# def get_data():
#     """Retrieve all data from the linked list."""
#     data = linked_list.get_data()
#     return {"linked_list": data}


# @app.post("/add-at-beginning/")
# def add_at_beginning(data: str = Query(None)):
#     """
#     Add a node at the beginning of the linked list.
#     Parameters:
#         data (str): Data for the new node.
#     """
#     if data is None:
#         log_and_raise_exception("Data is null. Cannot add node at the beginning.")
#     message = linked_list.add_at_beginning(data)
#     return {"message": message}


# @app.post("/add-at-end/")
# def add_at_end(data: str = Query(None)):
#     """
#     Add a node at the end of the linked list.
#     Parameters:
#         data (str): Data for the new node.
#     """
#     if data is None:
#         log_and_raise_exception("Data is null. Cannot add node at the end.")
#     message = linked_list.add_at_end(data)
#     return {"message": message}


# @app.put("/update-node/")
# def update_node(old_data: str = Query(None), new_data: str = Query(None)):
#     """
#     Update a node's value in the linked list.
#     Parameters:
#         old_data (str): The current value to update.
#         new_data (str): The new value to set.
#     """
#     if old_data is None or new_data is None:
#         log_and_raise_exception("Old data or new data is null. Cannot update node.")
#     message = linked_list.update_node(old_data, new_data)
#     return {"message": message}


# @app.delete("/delete-node/")
# def delete_node(data: str = Query(None)):
#     """
#     Delete a node from the linked list.
#     Parameters:
#         data (str): The value of the node to delete.
#     """
#     if data is None:
#         log_and_raise_exception("Data is null. Cannot delete node.")
#     message = linked_list.delete_node(data)
#     return {"message": message}


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


@app.get("/")
def read_root():
    info("Root endpoint accessed.")
    return {"message": "Welcome to the Linked List API!"}


@app.get("/get-data/")
def get_data():
    """Retrieve all data from the linked list."""
    try:
        data = linked_list.get_data()
        info(f"Retrieved linked list data: {data}")
        return {"linked_list": data}
    except Exception as e:
        error(f"Error retrieving data: {str(e)}")
        raise HTTPException(status_code=500, detail="An error occurred while retrieving data.")


@app.post("/add-at-beginning/")
def add_at_beginning(data: str = Query(None)):
    """
    Add a node at the beginning of the linked list.
    Parameters:
        data (str): Data for the new node.
    """
    if data is None:
        exception("Data is null. Cannot add node at the beginning.")
        raise HTTPException(status_code=400, detail="Data is null. Cannot add node at the beginning.")
    message = linked_list.add_at_beginning(data)
    info(f"Successfully added {data} at the beginning of the linked list.")
    return {"message": message}


@app.post("/add-at-end/")
def add_at_end(data: str = Query(None)):
    """
    Add a node at the end of the linked list.
    Parameters:
        data (str): Data for the new node.
    """
    if data is None:
        exception("Data is null. Cannot add node at the end.")
        raise HTTPException(status_code=400, detail="Data is null. Cannot add node at the end.")
    message = linked_list.add_at_end(data)
    info(f"Successfully added {data} at the end of the linked list.")
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
        exception("Old data or new data is null. Cannot update node.")
        raise HTTPException(status_code=400, detail="Old data or new data is null. Cannot update node.")
    message = linked_list.update_node(old_data, new_data)
    if "Updated" in message:
        info(f"Successfully updated node from {old_data} to {new_data}.")
    else:
        error(f"Update failed: {message}")
    return {"message": message}


@app.delete("/delete-node/")
def delete_node(data: str = Query(None)):
    """
    Delete a node from the linked list.
    Parameters:
        data (str): The value of the node to delete.
    """
    if data is None:
        exception("Data is null. Cannot delete node.")
        raise HTTPException(status_code=400, detail="Data is null. Cannot delete node.")
    message = linked_list.delete_node(data)
    if "Deleted" in message:
        info(f"Successfully deleted node with data {data}.")
    else:
        error(f"Delete failed: {message}")
    return {"message": message}


@app.get("/last-node/")
def get_last_node():
    """Get the last node of the linked list."""
    if linked_list.head is None:
        warning("Linked list is empty. Cannot retrieve the last node.")
        raise HTTPException(status_code=400, detail="Linked list is empty. Cannot retrieve the last node.")
    
    last_node_data = linked_list.get_last_node()
    info(f"The last node in the linked list is: {last_node_data}")
    return {"message": "Retrieved last node successfully.", "last_node": last_node_data}


@app.get("/reverse-list/")
def reverse_list():
    """Get a reversed view of the linked list."""
    if linked_list.head is None:
        error("Cannot reverse the list. The linked list is empty.")
        raise HTTPException(status_code=400, detail="The linked list is empty. Cannot reverse the empty list.")
    
    if linked_list.head.next is None:
        warning("Linked list has only one node; no need to reverse.")
        return {
            "message": "Linked list has only one node; no need to reverse.",
            "reversed_list": linked_list.get_data(),
        }
    
    reversed_data = linked_list.get_reversed_data()
    info(f"Successfully reversed linked list data: {reversed_data}")
    return {"message": "Linked list reversed successfully.", "reversed_list": reversed_data}