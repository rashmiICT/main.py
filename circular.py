# node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# class Linked List
class LinkedList:
    def __init__(self):
        self.head = None

        # Add new element at the start of the list

    def addBegging(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
            return
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = newNode
            newNode.next = self.head
            self.head = newNode

    # Add new element at the end of the list
    def addEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
            return
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = newNode
            newNode.next = self.head

            # Inserts a new element at the given position

    def push_at(self, newElement, position):
        newNode = Node(newElement)
        temp = self.head
        NoOfElements = 0
        if temp is not None:
            NoOfElements += 1
            temp = temp.next
        while temp != self.head:
            NoOfElements += 1
            temp = temp.next

        if position < 1 or position > (NoOfElements + 1):
            print("\nInvalid position.")
        elif position == 1:
            if self.head is None:
                self.head = newNode
                self.head.next = self.head
            else:
                while temp.next != self.head:
                    temp = temp.next
                newNode.next = self.head
                self.head = newNode
                temp.next = self.head
        else:
            temp = self.head
            for i in range(1, position - 1):
                temp = temp.next
            newNode.next = temp.next
            temp.next = newNode

    # Delete first node of the list
    def deleteBegging(self):
        if self.head is not None:
            if self.head.next == self.head:
                self.head = None
            else:
                temp = self.head
                firstNode = self.head
                while temp.next != self.head:
                    temp = temp.next
                self.head = self.head.next
                temp.next = self.head
                firstNode = None

        # Delete last node of the list

    def deleteEnd(self):
        if self.head is not None:
            if self.head.next == self.head:
                self.head = None
            else:
                temp = self.head
                while temp.next.next != self.head:
                    temp = temp.next
                lastNode = temp.next
                temp.next = self.head
                lastNode = None

        # Delete an element at the given position

    def pop_at(self, position):
        nodeToDelete = self.head
        temp = self.head
        NoOfElements = 0

        if temp is not None:
            NoOfElements += 1
            temp = temp.next
        while temp != self.head:
            NoOfElements += 1
            temp = temp.next

        if position < 1 or position > NoOfElements:
            print("\nInvalid position.")
        elif position == 1:
            if self.head.next == self.head:
                self.head = None
            else:
                while temp.next != self.head:
                    temp = temp.next
                self.head = self.head.next
                temp.next = self.head
                nodeToDelete = None

        else:
            temp = self.head
            for i in range(1, position - 1):
                temp = temp.next
            nodeToDelete = temp.next
            temp.next = temp.next.next
            nodeToDelete = None

    # display the content of the list

    def PrintList(self):
        temp = self.head
        if temp is not None:
            # print("\n\nThe list contains:", end=" ")
            while True:
                print(temp.data, ">>", end=" ")
                temp = temp.next
                if temp == self.head:
                    break
            print()
        else:
            print("The list is empty.")


# test the code
MyList = LinkedList()

# Add three elements at the start of the list.

print("------------------------------------------------------------------------\n")
print("add begging")
MyList.addBegging(30)
MyList.addBegging(20)
MyList.addBegging(10)
MyList.PrintList()



# Add three elements at the end of the list.

print("------------------------------------------------------------------------\n")
print("add end")
MyList.addEnd(40)
MyList.addEnd(50)
MyList.addEnd(60)
MyList.PrintList()

print("------------------------------------------------------------------------\n")
print("add pos")
# Insert an element at position 2
MyList.push_at(100, 1)
MyList.PrintList()

# Delete the first node

print("------------------------------------------------------------------------\n")
print("delete begging")
MyList.deleteBegging()
MyList.PrintList()

# Delete the last node

print("------------------------------------------------------------------------\n")
print("delete end")
MyList.deleteEnd()
MyList.PrintList()

print("------------------------------------------------------------------------\n")
print("delete pos")
# Delete an element at position
MyList.pop_at(3)
MyList.PrintList()


