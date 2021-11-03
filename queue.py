# Roy Yi
# 9/21/21
# Queue implementation using linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        n = Node(data)

        # empty list
        if not self.head:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def pop(self):
        if not self.head: return None
        val = self.head.data

        if not self.head.next:
            self.head = self.tail = None
        else:
            self.head = self.head.next

        return val
            
    def print_nodes(self):
        n = self.head
        while n:
            print(n.data)
            n = n.next

    def empty(self):
        return self.head == None

def main():
    a = LinkedList()
    
    for x in [3, 7, 5, 8, 10, 9]:
        a.push(x)

    while not a.empty():
        print(a.pop())

    # a.print_nodes()

if __name__ == "__main__":
    main()
