# Roy Yi
# 9/21/21
# Linked List in Python (stack)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        # set the head to the new node, and set its next pointer to the old head
        n = self.head
        self.head = Node(data)
        self.head.next = n

    def print_nodes(self):
        n = self.head
        while n:
            print(n.data)
            n = n.next

def main():
    a = LinkedList()
    
    for x in [3, 7, 5, 8, 10, 9]:
        a.push(x)

    a.print_nodes()

if __name__ == "__main__":
    main()
