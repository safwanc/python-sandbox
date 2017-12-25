class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return other == self.value
    
    def __str__(self):
        return self.value

class LinkedList(object):
    def __init__(self):
        self.root_node = None
    
    def __len__(self):
        length = 0
        node = self.root_node
        while node is not None:
            length += 1
            node = node.next
        return length

    def __iter__(self):
        node = self.root_node
        while node is not None:
            yield node
            node = node.next
    
    def __str__(self):
        return ' -> '.join(str(node) for node in self)

    @property
    def head(self):
        return self.root_node

    @property
    def tail(self):
        node = self.root_node
        while node.next is not None:
            node = node.next
        return node

    @property
    def empty(self):
        return len(self) == 0

    def add(self, item):
        if isinstance(item, LinkedListNode):
            node = item
        else:
            node = LinkedListNode(item)
        
        if self.root_node is None:
            self.root_node = node
        else:
            self.tail.next = node
    
    def remove(self, item):
        previous_node, current_node = (None, self.root_node)
        while current_node is not None:
            if current_node == item:
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.root_node = current_node.next
                return True
            previous_node = current_node
            current_node = current_node.next
        return False

    def reverse(self):
        previous_node, current_node, next_node = (None, self.root_node, None)
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.root_node = previous_node

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add('A')
    linked_list.add('B')
    linked_list.add('C')
    print(linked_list, '({} nodes)'.format(len(linked_list)))

    assert('A' in linked_list)
    assert('D' not in linked_list)

    linked_list.reverse()
    print(linked_list)

    assert(linked_list.remove('B'))
    print(linked_list)
    assert(linked_list.remove('A'))
    print(linked_list)
    assert(not linked_list.remove('D'))
    assert(linked_list.remove('C'))
    assert(linked_list.empty)

    linked_list.reverse()
    print(linked_list)

    linked_list.add('D')
    linked_list.reverse()
    print(linked_list)