from lista import LinkedList
from typing import Any


class Stack:
    _storage: LinkedList

    def __init__(self):
        self._storage = []

    def push(self, element: Any) -> None:
        self._storage.append(element)

    def pop(self)-> Any:
        return self._storage.pop()

    def len(self):
        lenght = 0
        for i in self._storage:
            lenght+=1
        return lenght

    def print(self):
        for i in self._storage:
            print(i)

stack = Stack()

print(stack)

assert stack.len() == 0

# stack.push(5)
# stack.push(4)
# stack.push(7)
#
# print("length = ", stack.len())
#
# stack.pop()
#
# print("length = ", stack.len())
#
# stack.push(1)
# stack.push(7)
#
# stack.print()

stack.push(3)
stack.push(10)
stack.push(1)

assert stack.len() == 3

stack.print()

print("szczytowa wartosc", stack.pop())

stack.print()

assert stack.len() == 2

print("lenght", stack.len())
