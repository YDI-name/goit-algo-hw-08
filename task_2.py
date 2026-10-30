class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def tree_sum(root):
    """
    Функція для знаходження суми всіх значень у двійковому дереві.
    """
    if root is None:
        return 0

    return root.val + tree_sum(root.left) + tree_sum(root.right)


root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.right = Node(20)

total_sum = tree_sum(root)
print(f"Сума всіх значень у дереві: {total_sum}")
