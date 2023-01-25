class LinkedList:
    def __init__(self, head):
        n = Node(head)
        self.head = n
        self.current = n
        self.size = 0

    def append(self, node):
        n = Node(node)
        self.current.next = n
        self.current = n
        self.size += 1

    def index(self, obj):
        current = self.head
        i = 0
        while current is not None:
            if current.data == obj:
                return i
            current = current.next
            i += 1
        return None

    def reverse(self, node):
        if (node == None):
            return node
        if (node.next == None):
            return node
        node1 = self.reverse(node.next)
        node.next.next = node
        node.next = None
        return node1

    def get(self, index):
        if index > self.size:
            return None
        else:
            current = self.head
            for i in range(index):
                current = current.next
            return current

    def clear(self):
        self.current = self.head
        self.size = 0

    def find(self, obj):
        current = self.head
        while current is not None:
            if current.data == obj:
                return current
            current = current.next
        return None

    def length(self):
        return self.size

    def pop(self, index):
        if index > self.size:
            return None
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next
            self.size -= 1

    def insert(self, index, obj):
        if index > self.size:
            return None
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            n = Node(obj)
            n.next = current.next
            current.next = n
            self.size += 1

    def remove(self, obj):
        current = self.head
        i = 0
        while current is not None:
            if current.data == obj:
                self.pop(i)
            current = current.next
            i += 1

    def write(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def main_glatzl():
    l = LinkedList(1)
    for i in range(2, 10):
        l.append(i)
    l.pop(5)
    l.remove(8)
    l.write()
    print(f"Size: {l.length()}")
    l.head = l.reverse(l.head)
    l.write()

if __name__ == '__main__':
    main_glatzl()
