# ============================================================
# ASSESSMENT 3.6: DFS METHODS IN BINARY TREE
# NAME: DELA CUESTA
# LETTERS: D E L A C U E S T A
# ============================================================


class Node:
    """Represents one node in the binary tree."""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """Creates the DELACUESTA tree and runs DFS traversals."""

    def __init__(self):
        self.root = None

    def build_tree(self):
        # Same binary-tree arrangement used in Assessment 3.4
        self.root = Node("D")

        self.root.left = Node("E")
        self.root.right = Node("L")

        self.root.left.left = Node("A")
        self.root.left.right = Node("C")

        self.root.right.left = Node("U")
        self.root.right.right = Node("E")

        self.root.left.left.left = Node("S")
        self.root.left.left.right = Node("T")

        self.root.left.right.left = Node("A")

    # DFS METHOD 1: ROOT -> LEFT -> RIGHT
    def preorder(self, node, result):
        if node is not None:
            result.append(node.data)
            self.preorder(node.left, result)
            self.preorder(node.right, result)

    # DFS METHOD 2: LEFT -> ROOT -> RIGHT
    def inorder(self, node, result):
        if node is not None:
            self.inorder(node.left, result)
            result.append(node.data)
            self.inorder(node.right, result)

    # DFS METHOD 3: LEFT -> RIGHT -> ROOT
    def postorder(self, node, result):
        if node is not None:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.data)

    def display_tree(self):
        print("                 D")
        print("               /   \\")
        print("              E     L")
        print("             / \\   / \\")
        print("            A   C U   E")
        print("           / \\  /")
        print("          S   T A")

    def run(self):
        self.build_tree()

        preorder_result = []
        inorder_result = []
        postorder_result = []

        self.preorder(self.root, preorder_result)
        self.inorder(self.root, inorder_result)
        self.postorder(self.root, postorder_result)

        print("=" * 58)
        print("             ASSESSMENT 3.6: DFS METHODS")
        print("                    DELA CUESTA")
        print("=" * 58)

        print("\nBINARY TREE STRUCTURE:")
        self.display_tree()

        print("\n" + "-" * 58)
        print("DEPTH-FIRST SEARCH TRAVERSALS")
        print("-" * 58)

        print("\n1. PREORDER  (ROOT - LEFT - RIGHT)")
        print("   " + " -> ".join(preorder_result))

        print("\n2. INORDER   (LEFT - ROOT - RIGHT)")
        print("   " + " -> ".join(inorder_result))

        print("\n3. POSTORDER (LEFT - RIGHT - ROOT)")
        print("   " + " -> ".join(postorder_result))

        print("\n" + "=" * 58)
        print("                 PROGRAM FINISHED")
        print("=" * 58)


if __name__ == "__main__":
    tree = BinaryTree()
    tree.run()
