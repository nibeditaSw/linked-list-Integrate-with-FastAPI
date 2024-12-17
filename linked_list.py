class Node:
    """Class representing a node in the linked list."""

    def __init__(self, data):
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
