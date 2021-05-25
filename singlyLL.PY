print("\n\n\t\t \033[1;36;65m   create singly linked list\n\n")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class singlyLinkList:
    def __init__(self):
        self.head = None

    def listLength(self):
        temp = self.head
        count = 0
        while temp is not None:
            count = count + 1
            temp = temp.next
        return count

    def insertBegging(self, data):
        new_big = Node(data)
        new_big.next = self.head
        self.head = new_big




    def insertEnd(self, data):
        new_end = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_end



    def add_Pos(self, pos, data):
        new_pos = Node(data)
        temp = self.head
        for i in range(pos - 1):
            temp = temp.next
        new_pos.data = data
        new_pos.next = temp.next
        temp.next = new_pos



    def delete_beggining(self):
        temp = self.head
        self.head = temp.next
        temp.next = None



    def delete_End(self):
        temp = self.head.next
        prev = self.head
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None



    def deletePos(self, pos):
        temp = self.head.next
        prev = self.head
        for i in range(pos - 1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None




    def display(self):
        if self.head is None:
            print("linked list is empty")

        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next





print("------------------------------------------------------------------------\n")

L = singlyLinkList()
L.display()


print("------------------------------------------------------------------------\n")
print("\033[1;31;65m  create nodes")
n = Node(10)
L.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.next = n2
L.display()
x = L.listLength()
print("\nlength is ", x)

print("------------------------------------------------------------------------\n")
print("add begging")
L.insertBegging(5)
L.insertBegging(3)
L.display()
x = L.listLength()
print("\nlength is ", x)

print("------------------------------------------------------------------------\n")
print("add end")
L.insertEnd(40)
L.insertEnd(50)
L.display()
x = L.listLength()
print("\nlength is ", x)

print("------------------------------------------------------------------------\n")
print("add pos")
L.add_Pos(2, 15)
L.add_Pos(5, 25)
L.display()
x = L.listLength()
print("\nlength is ", x)

print("------------------------------------------------------------------------\n")
print("delete begging")
L.delete_beggining()
L.display()
x = L.listLength()
print("\nlength is ", x)

print("------------------------------------------------------------------------\n")
print("delete end")
L.delete_End()
L.display()
x = L.listLength()
print("\nlength is ", x)

print("------------------------------------------------------------------------\n")
print("delete pos")
L.deletePos(1)
L.display()
x = L.listLength()
print("\nlength is ", x)

print("\n------------------------------------------------------------------------\n")
print("count length")
x = L.listLength()
print("length is  ", x)
