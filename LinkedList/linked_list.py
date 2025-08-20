class Node:
    def __init__(self , data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_box = Node(data)

        if self.head is None:
            self.head = new_box
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_box

    def display(self):
        current =  self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")


train = LinkedList()
train.append(10)
train.append(20)
train.append(40)

train.display()