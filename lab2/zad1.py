from typing import Any

class Node:
    value: Any
    next: 'Node'

    def __init__(self, value: Any, next: 'Node') -> None:
        self.value = value
        self.next = next


class LinkedList:
    head: Node
    tail: Node

    def __init__(self, head: Node,tail: Node )-> None:
        self.head = head
        self.tail = tail


    def push(self, value: Any) -> None:
        self.head == value

    def append(self, value: Any) -> None:
        self.tail

    def __str__(self):
        return 'head: {0}, tail: {1}' \
            .format(self.head, self.tail)


list_:LinkedList = LinkedList(None, None)


assert list_.head == None

list_.push(1)

list_.push(0)

assert str(list_) == '0 -> 1'
