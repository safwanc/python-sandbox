'''
Convert BST so each node will be the sum of all nodes that are greater than its original value

   2           3
1    3   ==> 5    0
'''

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

def convert_tree(node):
    current, stack, current_sum = node, [], 0

    while current or stack:
        if current is not None:
            stack.append(current)
            current = current.right
        else:
            current = stack.pop()
            temp = current.value
            current.value = current_sum
            current_sum += temp
            current = current.left
    
    return node

def convert_tree_recursive(node, current_sum=0):
    if not node: return current_sum

    current_sum = convert_tree_recursive(node.right, current_sum)
    
    current_value = node.value
    node.value = current_sum
    current_sum += current_value
    
    convert_tree_recursive(node.left, current_sum)

    return current_sum


if __name__ == '__main__':
    root = BinaryTreeNode(2, BinaryTreeNode(1), BinaryTreeNode(3))
    print('Before: \n', root)

    convert_tree_recursive(root)
    print('After: \n', root)