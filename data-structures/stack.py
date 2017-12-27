'''A stack (LIFO) implemented with a linked list'''

class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack(object):
    def __init__(self):
        self.count = 0
        self.root_node = None
    
    def __len__(self):
        return self.count

    def __iter__(self):
        node = self.root_node
        while node is not None:
            yield node.value
            node = node.next

    def __str__(self):
        contents = '[Stack: '
        contents += ' | '.join(str(node) for node in self)
        return contents + ']'
        
    @property
    def empty(self):
        return len(self) == 0

    def push(self, item):
        node = LinkedListNode(item)
        node.next = self.root_node
        self.root_node = node
        self.count += 1
    
    def pop(self):
        if self.empty:
            return None

        node = self.root_node
        self.root_node = node.next
        self.count -= 1
        return node.value

    def peek(self):
        if self.empty:
            return None
        return self.root_node.value

if __name__ == '__main__':
    stack = Stack()
    assert(stack.empty)

    stack.push(1)
    assert(not stack.empty)

    stack.push(2)
    print(stack)
    assert(stack.peek() == 2)

    print('Popped: ', stack.pop())
    print(stack)
    assert(len(stack) == 1)

    print('Popped: ', stack.pop())
    print(stack)
    assert(stack.empty)
    assert(stack.pop() is None)
    assert(stack.peek() is None)