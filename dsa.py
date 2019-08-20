class Node:
    def __init(self):
        self.data = None
        self.next = None
    def set_data(self,data):
        self.data = data
    def get_data(self):
        return self.data
    def set_next(self,next):
        self.next = next
    def get_next(self):
        return self.next
    def has_next(self):
        return self.next !=None
    def list_length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = head.get_next()
        return count
head = Node()
head.set_data(5)
node2 = Node()
node2.set_data(10)
node3 = Node()
node3.set_data(15)
print(head.get_data())
print(node2.get_data())
print(node3.get_data())
head.set_next(node2.get_data())
node2.set_next(node3.get_data())
node3.set_next(None)

print(head.get_next())
print(node2.get_next())
print(node3.get_next())


