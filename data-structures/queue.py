'''Queue (FIFO) implemented with two stacks (LIFO)'''

class Queue(object):
    def __init__(self):
        self.in_stack = list()
        self.out_stack = list()

    def __str__(self):
        return 'In Stack: {}\nOut Stack: {}'.format(self.in_stack, self.out_stack)

    def __len__(self):
        return len(self.in_stack) + len(self.out_stack)

    @property
    def empty(self):
        return len(self) == 0

    def enqueue(self, item):
        self.in_stack.append(item)
    
    def dequeue(self):
        if self.empty:
            return None

        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                self.out_stack.append(self.in_stack.pop())

        return self.out_stack.pop()

    def peek(self):
        if self.empty:
            return None

        if len(self.out_stack) > 0:
            return self.out_stack[-1]
        else:
            return self.in_stack[-1]

if __name__ == '__main__':
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    assert(len(queue) == 2)
    print(queue)
    print(queue.peek())

    print(queue.dequeue())
    assert(len(queue) == 1)
    print(queue)
    print(queue.peek())
    
    print(queue.dequeue())
    assert(len(queue) == 0)
    assert(queue.dequeue() is None)
