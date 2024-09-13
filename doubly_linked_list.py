class Node:
    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev = prev_node
        self.next = next_node

    def __repr__(self):
        return "<Node data: %s>" % self.data

class DoublyLinkedList:
    """
    A linked list is a data structure optimized to remove and insert data.
    """

    def __repr__(self):
        if self.is_empty():
            return "[Empty List]"

        current = self.head
        content = "[Head: %s]" % current.data

        while current.next:
            current = current.next
            if current.next == None:
                content += " -> [Tail: %s]" % current.data
            else:
                content += " -> [%s]" % current.data

        return content

    def __init__(self):
        self.head = None
        self.tail = None
        self.__count = 0

    def is_empty(self):
        return self.__count == 0

    def __len__(self):
        return self.__count

    def add(self, data):
        newNode = Node(data)
        
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
        elif self.head.next == None:
            self.tail = newNode
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode 
        
        self.__count += 1

    def remove(self, target):
        if self.is_empty():
            raise Exception('Cant remove from an empty list')
        
        current = self.head

        while current:
            if current.data == target:
                if self.__count == 1:
                    self.head = None
                    self.tail = None
                elif current.prev == None:
                    self.head = self.head.next 
                elif current.next == None:
                    current.prev.next = None
                    self.tail = current.prev
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                self.__count -= 1
            current = current.next

l = DoublyLinkedList()
l.add(1)
print('List can add:', l)
l.add(2)
l.add(4)
l.add(80)
print('List can add multilple data:', l)
l.remove(2)
print('List can remove:', l)
l.remove(4)
l.remove(80)
l.remove(1)
print('List empty without data:', l)





