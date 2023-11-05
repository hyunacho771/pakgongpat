class Node:
    def __init__(self, data):
        self.data=data
        self.prev=None
        self.next=None

class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def append(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.prev=self.tail
            self.tail.next=new_node
            self.tail=new_node

    def printlist(self):
        current=self.head
        while current:
            print(current.data, end=' -> ')
            current=current.next
        print("null")

if __name__ == "__main__":
    myList=DoubleLinkedList()
    print("첫번째 숫자를 입력하세요")
    a=input()
    print("두번째 숫자를 입력하세요")
    b=input()
    print("세번째 숫자를 입력하세요")
    c=input()
    myList.append(a)
    myList.append(b)
    myList.append(c)

    myList.printlist()