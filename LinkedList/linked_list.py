from logging import exception


class Node:
    def __init__(self , data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert elements at the end
    def append(self,data):
        new_box = Node(data)

        if self.head is None:
            self.head = new_box
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_box

    # Insert elements at the beginning
    def insert_at_beginning(self,data):
        new_box = Node(data)
        new_box.next = self.head
        self.head = new_box

    # Insert a set of data(dataList)
    def insert_data_list(self, data_list):
        self.head = None
        for data in data_list:
            self.append(data)

    # Get length of the linked list
    def get_length(self):
        count = 0
        current = self.head
        while current:
            count+=1
            current = current.next
        return count

    # Remove the element at the specific index
    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        current = self.head
        while current:
            if count == index - 1:
                current.next = current.next.next
                break
            current = current.next
            count+=1

    # Insert elements at the specific index
    def insert_at_specific_index(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        current = self.head
        while current:
            if count == index - 1:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next
            count+=1


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
train.insert_at_beginning(5)
train.insert_data_list(["banana" , "mango" , "apple"])
train.display()

print("Length : " ,train.get_length())
train.remove_at(2)
train.display()

train.insert_at_specific_index(1 , "cherry")
train.display()
train.insert_at_specific_index(0 , "fig")
train.display()
