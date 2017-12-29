class BinaryTreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert_left(self, value):
        if self.left: raise RuntimeError('Left node already exists')
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        if self.right: raise RuntimeError('Right node already exists')
        self.right = BinaryTreeNode(value)
        return self.right

    def __str__(self, depth=0):
        string = ""
        if self.right != None: string += self.right.__str__(depth + 1)
        string += "\n" + ("    " * depth) + str(self.value)
        if self.left != None: string += self.left.__str__(depth + 1)
        return string

class IterativeTraversal(object):

    @staticmethod
    def bfs(root):
        queue, visited = [root], []
        while queue:
            node = queue.pop()
            visited.append(node.value)
            if node.left: queue.insert(0, node.left)
            if node.right: queue.insert(0, node.right)
        return visited

    @staticmethod
    def dfs_preorder(root):
        stack, visited = [root], []
        while stack:
            node = stack.pop()
            visited.append(node.value)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        return visited

    @staticmethod
    def dfs_inorder(root):
        current, stack, visited = root, [], []
        while current or stack:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                visited.append(current.value)
                current = current.right
        return visited

    @staticmethod
    def dfs_postorder(root):
        stack, visited, accounted_for = [root], [], set()

        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                visited.append(node.value)
                accounted_for.add(node)
            else:
                left_child_visited = node.left in accounted_for if node.left else True
                right_child_visited = node.right in accounted_for if node.right else True

                if left_child_visited and right_child_visited:
                    visited.append(node.value)
                    accounted_for.add(node)
                else:
                    stack.append(node)
                    if node.right: stack.append(node.right)
                    if node.left: stack.append(node.left)

        return visited
    
    @staticmethod
    def tree_height(root):
        queue, height = [root], 0
        while queue:
            nodes_at_this_level = len(queue)
            if nodes_at_this_level == 0: break
            height += 1
            for _ in range(nodes_at_this_level):
                node = queue.pop(0)
                if node.left:  queue.append(node.left)
                if node.right: queue.append(node.right)
        return height

class RecursiveTraversal(object):
    @staticmethod
    def dfs_preorder(node, result=list()):
        if not node: return
        result.append(node.value)
        RecursiveTraversal.dfs_preorder(node.left, result)
        RecursiveTraversal.dfs_preorder(node.right, result)
        return result

    def dfs_inorder(node, result=list()):
        if not node: return
        RecursiveTraversal.dfs_inorder(node.left, result)
        result.append(node.value)
        RecursiveTraversal.dfs_inorder(node.right, result)
        return result

    def dfs_postorder(node, result=list()):
        if not node: return
        RecursiveTraversal.dfs_postorder(node.left, result)
        RecursiveTraversal.dfs_postorder(node.right, result)
        result.append(node.value)
        return result

    @staticmethod
    def tree_height(node):
        if not node: return 0
        return max(RecursiveTraversal.tree_height(node.left), RecursiveTraversal.tree_height(node.right)) + 1


if __name__ == '__main__':
    root = BinaryTreeNode(1, BinaryTreeNode(2, BinaryTreeNode(4), BinaryTreeNode(5)), BinaryTreeNode(3, None, BinaryTreeNode(6)))
    print(root)

    print('-- Iterative Solutions')
    print('Height', IterativeTraversal.tree_height(root))
    print('BFS', IterativeTraversal.bfs(root))
    print('DFS Preorder', IterativeTraversal.dfs_preorder(root))
    print('DFS Inorder', IterativeTraversal.dfs_inorder(root))
    print('DFS Postorder', IterativeTraversal.dfs_postorder(root))

    print('-- Recursive Solutions')
    print('Height', RecursiveTraversal.tree_height(root))
    print('DFS Preorder', RecursiveTraversal.dfs_preorder(root))
    print('DFS Inorder', RecursiveTraversal.dfs_inorder(root))
    print('DFS Inorder', RecursiveTraversal.dfs_postorder(root))