from typing import Any

class Node:
    value: Any
    next: 'Node'

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        return str(self.head) + "->" +  str(self.tail)

    def push(self, value: Any) -> None:
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def append(self,value: Any) -> None:
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = node

    def node(self, at:int) -> None:
        if at >= self.len():
            return None
        i = 0
        node = self.head
        while True:
            if i == at:
                return node.value
            i += 1
            node = node.next

    def insert(self, value: Any, after: Node) -> None:
        # new = Node(value)
        after = Node(value)
        # new.next = after.next.next
        # after.next = new
        
        node = Node(value)
        node.next = after.next
        after.next = node

    def pop(self) -> Any:
        if self.head == None:
            print("lista jest pusta")
        else:
            tmp = self.head.value
            self.head = self.head.next
            return tmp

    def remove_last(self) -> Any:
        last = self.head
        while last.next.next != None:
            last = last.next
        tmp = last.next
        last.next = None
        return tmp.value

    def remove(self,after: Node) -> Any:
        head = self.head

        while head.next != None:
            if head.next.value == after:
                head = head.next
            head.next = head.next.next

    def print(self):
        element = self.head
        while element != None:
            print(element.value, end = "->")
            element = element.next
        print("None")

    def len(self):
        length = 0
        pom = self.head
        while pom != None:
            length += 1
            pom = pom.next
        return length




list_ = LinkedList()
assert list_.head == None

list_.push(1)
list_.push(0)

list_.append(9)
list_.append(10)
print(list_.len())
list_.print()

print(list_.node(2))
# assert str(list_) == '0 -> 1'

middle_node = list_.node(1)
list_.insert(5, middle_node)
# list_.insert(5,1)
list_.print()

print(list_.pop())
list_.print()

print(list_.remove_last())
# list_.remove_last()
list_.print()

list_.remove(1)
list_.print()
