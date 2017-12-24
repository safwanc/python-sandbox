TERMINATING_CHAR = '*'

class Trie():
    def __init__(self):
        self.root_node = dict()
    
    def add_word(self, word):
        node = self.root_node
        for char in word:
            if char not in node:
                node[char] = dict()
            node = node[char]
        node[TERMINATING_CHAR] = dict()
            
    def __contains__(self, word):
        node = self.root_node
        for char in word:
            if char in node:
                node = node[char]
            else:
                return False
        return TERMINATING_CHAR in node

    def __str__(self):
        def concatenate(node, indent=0):
            string = str()
            for key, value in node.items():
                string += '\n{space}{char}:'.format(space='\t' * indent , char=key)
                string += concatenate(value, indent + 1)
            return string
        return concatenate(self.root_node)

if __name__ == '__main__':
    trie = Trie()
    trie.add_word('a')
    trie.add_word('ab')
    trie.add_word('ac')
    trie.add_word('acba')
    trie.add_word('ab')

    print(trie)
    print('acba' in trie)
    print('abcd' not in trie)
