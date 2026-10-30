class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    """
    Додає новий вузол у двійкове дерево пошуку.
    """
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def find_min(root):
    """
    Знаходить найменше значення у двійковому дереві пошуку.
    Повертає None, якщо дерево порожнє.
    """
    if root is None:
        return None

    current = root
    # Рухаємося до найлівішого вузла
    while current.left is not None:
        current = current.left

    return current.val


# Практичне застосування
if __name__ == "__main__":
    root = Node(50)
    values_to_insert = [30, 20, 40, 70, 60, 80]
    for val in values_to_insert:
        insert(root, val)

    print(f"Значення, додані в дерево: 50 (корінь) та {values_to_insert}")

    # Знаходимо найменше значення
    min_value = find_min(root)
    print(f"Найменше значення у дереві: {min_value}")
