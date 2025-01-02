class Node:
    """Class representing a node in the linked list."""

    def __init__(self, data):
        """
        Constructor to initialize the node object.

        Parameters:
            data (any): The data to be stored in the node.
        """
        self.data = data
        self.next = None


class LinkedList:
    """Class representing the linked list."""

    def __init__(self):
        self.head = None

    def get_data(self):
        """Retrieve all data from the linked list."""
        data_list = []
        current = self.head
        while current:
            data_list.append(current.data)
            current = current.next
        return data_list

    def add_at_beginning(self, data):
        """Add a node at the beginning of the linked list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return f"Added {data} at the beginning."

    def add_at_end(self, data):
        """Add a node at the end of the linked list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return f"Added {data} as the first node."
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        return f"Added {data} at the end."

    def update_node(self, old_data, new_data):
        """Update a node's value in the linked list."""
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                return f"Updated node from {old_data} to {new_data}."
            current = current.next
        return f"Node with data {old_data} not found."

    def delete_node(self, data):
        """Delete a node from the linked list."""
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return f"Deleted node with data {data}."   # Deleting the Head Node
        prev = None
        while current:
            if current.data == data:
                prev.next = current.next
                return f"Deleted node with data {data}."  # Deleting a Middle or Last Node
            prev = current
            current = current.next
        return f"Node with data {data} not found."


    def get_last_node(self):
        """Retrieve the last node's data from the linked list."""
        if self.head is None:
            return None
        
        current = self.head
        while current.next:
            current = current.next
        return current.data
    
    
    def get_reversed_data(self):
        """Retrieve the data from the linked list in reversed order without modifying the list."""
        data_list = []
        current = self.head
        while current:
            data_list.append(current.data)
            current = current.next
        return data_list[::-1]  
    
