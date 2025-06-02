class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

        
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def delete_with_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        current_node = self.head
        while current_node:
            if current_node.data == data:
                if current_node.next:
                    current_node.next.prev = current_node.prev
                if current_node.prev:
                    current_node.prev.next = current_node.next
                return
            current_node = current_node.next

    def display_forward(self):
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(current_node.data)
            current_node = current_node.next
        print("Doubly Linked List (forward):", nodes)

    def display_backward(self):
        nodes = []
        current_node = self.head
        while current_node and current_node.next:
            current_node = current_node.next
        while current_node:
            nodes.append(current_node.data)
            current_node = current_node.prev
        print("Doubly Linked List (backward):", nodes)
        
dll = DoublyLinkedList()

dll.append(1)
dll.append(2)
dll.append(3)

dll.prepend(0)

dll.display_forward()
dll.display_backward()

dll.delete_with_value(2)

dll.display_forward()
dll.display_backward()

print("hello world")