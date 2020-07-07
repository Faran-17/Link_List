""" Below is the code for the implementation of link list"""


class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):  # head of the link list
        self.head = None

    def insert_at_beginig(self, data):   # puts the data at in reverse order
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr =  self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):  # Insert the data from left to right like default
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next  # Keep iterating till reach the end of the link list

        itr.next = Node(data, None)

    def insert_values(self, data_list):  # new list
        self.head = None   # clears the value of the current list
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):  # Gives the length of the link list
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index ")

        if index == 0:
            self.head = self.head.next  # if the first element is removed then
            return                      # second element becomes the head

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:  # stop at the element before the actual element we want to remove
                itr.next = itr.next.next  # linking the element with the next of the next element
                break
            else:
                itr = itr.next
                count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginig(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data, itr.next)
                itr.next = node
                break
            else:
                itr = itr.next
                count += 1


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginig(5)
    ll.insert_at_beginig(89)
    ll.insert_at_end(79)
    ll.insert_at_end(7)
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    print("Length of the list is ", ll.get_length())
    ll.remove_at(2)
    ll.print()
    ll.insert_at(0, "Figs")
    ll.insert_at(2, "Apple")
    ll.print()

    
# OUTPUT   
# banana-->mango-->grapes-->orange-->
# Length of the list is  4
# banana-->mango-->orange-->
# Figs-->banana-->Apple-->mango-->orange-->
