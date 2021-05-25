print("\n\n\t\t \033[1;31;65m  create doubly linked list\n\n")

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL():
    def __init__(self):
        self.head = None

    def listLength(self):
        temp = self.head
        count = 0
        while temp is not None:
            count = count + 1
            temp = temp.next
        return count



    def addBig(self, data):
        newNode = Node(data)
        temp = self.head
        temp.prev = newNode
        newNode.next = temp
        self.head = newNode

    def addEnd(self, data):
        newEnd = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newEnd
        newEnd.prev = temp

    def addPos(self, pos, data):
        newPos = Node(data)
        temp = self.head
        for i in range(1, pos - 1):
            temp = temp.next
        newPos.prev = temp.next
        newPos.next = temp.next
        temp.prev = newPos
        temp.next = newPos

    def deleteBig(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.head.prev = None

    def delete_End(self):
        temp = self.head.next
        befor = self.head
        while temp.next is not None:
            temp = temp.next
            befor = befor.next
        befor.next = None
        temp.prev = None

    def deletePos(self, pos):
        temp = self.head.next
        befor = self.head
        for i in range(1, pos - 1):
            temp = temp.next
            befor = befor.next
        befor.next = temp.next
        temp.next.prev = befor
        temp.prev = None
        temp.prev = None

    def display(self):
        if self.head is None:
            print("doubly linked is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, ">>", end=" ")
                temp = temp.next




print("\033[1;31;65m ------------------------------------------------------------------------\n")

L = DLL()
L.display()

print("------------------------------------------------------------------------\n")
print("create nodes")
n1 = Node(10)
L.head = n1
n2 = Node(20)
n1.next = n2
n2.prev = n1
n3 = Node(30)
n2.next = n3
n3.prev = n2

L.display()
x = L.listLength()
print("\nlength is ", x)

print("\n---------------------------------------------------")
print("add begging")
L.addBig(5)
L.display()
x = L.listLength()
print("\nlength is ", x)

print("\n---------------------------------------------------")
print("add end")
L.addEnd(40)
L.display()
x = L.listLength()
print("\nlength is ", x)

print("\n---------------------------------------------------")
print("add pos")
L.addPos(3, 100)
L.display()
x = L.listLength()
print("\nlength is ", x)

print("\n---------------------------------------------------")
print("delete begging")
L.deleteBig()
L.display()
x = L.listLength()
print("\nlength is ", x)

print("\n---------------------------------------------------")
print("delete end")
L.delete_End()
L.display()
x = L.listLength()
print("\nlength is ", x)


print("\n---------------------------------------------------")
print("delete pos")
L.deletePos(2)
L.display()
x = L.listLength()
print("\nlength is ", x)
