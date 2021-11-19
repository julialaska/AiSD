from typing import Any, List

class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent: TreeNode = self
        self.left = None
        self.right = None

    def is_leaf(self) -> bool:
        if (self == None):
            return False

        if (self.left == None and self.right == None):
            return True

        return False


    def add(child: 'TreeNode') -> None:
        # self.children.append(child)
        if self.value:
            if child.value < self.value:
                if self.left is None:
                    self.left = TreeNode(child)
                else:
                    self.left.insert(child.value)
            elif child.value > self.value:
                if self.right is None:
                    self.right = TreeNode(child)
                else:
                    self.right.insert(child.value)
        else:
            self.value = child.value

        def deep_first(visit: Callable[['TreeNode'], None]):


