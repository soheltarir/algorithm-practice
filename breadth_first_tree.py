class Node:
    def __init__(self, key):
        self.data = key
        self.left, self.right = None, None


def print_level_order(root_node: Node):
    if not root_node:
        return
    queue = [root_node]
    while len(queue):
        print(queue[0].data)
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Level order traversal of binary tree is,")
    print(print_level_order(root))
