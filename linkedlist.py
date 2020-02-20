#Node
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def add(self,data):
        temp = self.head
        if(temp is None):
            self.head = Node(data)
            return
        while(temp.next):
            temp = temp.next
        temp.next = Node(data)
        return

    def deleteKey(self, data):
        current = self.head
        prev = None
        if(current is None):
            print("Deletion Not Performed. Error: Linked List is Empty")
        elif(current.data == data):
            self.head = current.next
            current = None
            print(f'{data} deleted!')
        else:
            while(current is not None):
                if(current.data == data):
                    break
                prev = current
                current = current.next
            if(current is None):
                print("Deletion Not Performed. Error: Element is not in the Linked List")
            else:
                print(f'{data} deleted!')
                prev.next = current.next
                current = None
        return

    def deleteAtPosition(self, pos):
        current = self.head
        pos = int(pos)
        if(current is None):
            print("Deletion Not Performed. Error: Linked List is Empty")
        elif(pos == 0):
            print(f"Deleting at {pos} Position!")
            self.head = self.head.next
            current = None
        else:
            for i in range(pos-1):
                current = current.next
            if(current is None or current.next is None):
                print("Deletion Not Performed. Error: Out of Index!")
            else:
                # print("current.next", current.next)
                print(f"Deleting at {pos} Position!", current.next.data)
                current.next = current.next.next

        return
    #     current = self.head
    #     pos = int(pos)
    #     if(current is None):
    #         print("Deletion Not Performed. Error: Linked List is Empty")
    #     elif(pos == 0):
    #         print(f"Deleting at {pos} Position!")
    #         self.head = self.head.next
    #         current = None
    #     else:
    #         posCount = 0
    #         while(posCount+1 != pos):
    #             current = current.next
    #             if(current is None):
    #                 break
    #             posCount += 1
                

    #         if(current is None or current.next is None):
    #             print("Deletion Not Performed. Error: Out of Index!")
    #             # return
    #             # print(temp)
    #         else:
    #             print(f"Deleting at {pos} Position!", current.next.data)
    #             current.next = current.next.next
    #     return


    

    def traverse(self):
        print("Traversing...")
        current = self.head
        if(current is None):
            print("Linked List is Empty")
            return
        while(current):
            print(current.data)
            current = current.next
        return

    def traverseRec(self, current = -1):
        if(current is None):
            return
        elif(current == -1):
            current = self.head
        print(current.data)
        self.traverseRec(current.next)
        return
        

    def deleteList(self):
        current = self.head
        while(current is not None):
            temp = current.next
            del current.data
            current = temp
        if(current is None):
            self.head = None
        return

    def listLength(self):
        length = 0
        current = self.head
        while(current):
            current = current.next
            length += 1
        return length

    def listLengthRecursion(self, current = -1):
        if(current is None):
            return 0
        if(current == -1):
            current = self.head
        return 1 + self.listLengthRecursion(current.next)    

    def search(self, data):
        current = self.head
        while(current):
            if(current.data == data):
                return True
            current = current.next
        return False

    def searchRec(self, data, current = -1):
        if(current is None):
            return False
        else:
            if(current == -1):
                current = self.head
                data = int(data)
            if(current.data == data):
                return True
            return self.searchRec(data, current.next)
    
    def getByPos(self, pos):
        current = self.head
        count = 0
        if pos > self.listLength()-1 or pos < 0:
            return "Invalid position"
        else:
            while(count != pos):
                current = current.next
                count += 1
            return current.data
        
    def getByPosFromEnd(self, pos):
        current = self.head
        count = 0
        if pos > self.listLength()-1 or pos < 0:
            return "Invalid position"
        else:
            while(count != self.listLength()-1-pos):
                current = current.next
                count += 1
            return current.data        

    def getMidElement(self):
        current = self.head
        mid = int(str((self.listLength()/2) + 1).split('.')[0])-1
        count = 0
        while count != mid:
            current = current.next
            count += 1
        return current.data

    def numberCount(self, key):
        current = self.head
        count = 0
        while current:
            if(current.data == key):
                count += 1
            current = current.next
        return count


ll = LinkedList()
ll.add(0)
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)

# print(ll.listLength())
# ll.traverse()
# ll.deleteList()
# print(ll.listLength())
# print(ll.listLengthRecursion())
# ll.traverseRec()
print(ll.numberCount(1))
# while True:
#     print(ll.searchRec(input("Search what? ")))
# print(ll.searchRec())
# ll.listLengthRecursion("Sds")
# ll.traverse()

# # ll.deleteKey(5)
# pos = input("Pos to delete: ")
# ll.deleteAtPosition(pos)
# ll.traverse()
# print(ll.head.data, ll.head.next)