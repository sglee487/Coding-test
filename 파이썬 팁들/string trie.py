# http://cd4761.blogspot.com/2017/02/trie-1.html
# http://cd4761.blogspot.com/2017/03/trie-2.html
import collections


class Node:
    def __init__(self, label=None, data=None):
        self.label = label
        self.data = data
        self.children = collections.defaultdict(Trie)
        self.NodeCount = 0

    def add_child(self, key, data=None):
        if not isinstance(key, Node):  # key가 Node의 instance가 아니면
            self.children[key] = Node(key, data)
        else:
            self.children[key.label] = key

    def __getitem__(self, key):
        return self.children[key]

    def __str__(self, depth=0):
        s = []
        for key in self.children:
            s.append('{}{} {}'.format(' ' * depth, key or '#', '\n'
                                      + self.children[key].__str__(depth + 1)))

        return ''.join(s)

class Trie:
    def __init__(self):
        self.head = Node()

    def __getitem__(self, key):
        return self.head.children[key]

    def __str__(self, depth=0):
        return self.head.__str__()

    def add(self, word):
        current_node = self.head
        word_finished = True

        for i in range(len(word)):
            if word[i] in current_node.children:
                current_node = current_node.children[word[i]]
            else:
                word_finished = False
                break

        if not word_finished:
            while i < len(word):
                current_node.add_child(word[i])
                current_node.NodeCount += 1
                current_node = current_node.children[word[i]]
                i += 1

        current_node.add_child(None)
        current_node.NodeCount += 1
        current_node = current_node.children[None]
        current_node.data = word

    def insert_word(self, word):
        for word in word.split():
            self.add(word)

    def search_with_prefix(self, prefix):
        words = list()

        if prefix is None:
            raise ValueError('Requires not-Null prefix')

        top_node = self.head

        for letter in prefix:
            if letter in top_node.children:
                top_node = top_node.children[letter]
            else:
                return words

        if top_node == self.head:
            queue = [node for key, node in top_node.children.items()]
        else:
            queue = [top_node]

        while queue:
            current_node = queue.pop()

            if current_node.data is not None:
                words.append(current_node.data)

            queue = [node for key, node in current_node.children.items()] + queue

        return words

    def delete_word(self, word, depth=0):
        current_node = self.head

        for letter in word[:-1]:
            if letter not in current_node.children:
                return False
            current_node = current_node.children[letter]

        if current_node.NodeCount > 1:
            del current_node.children[word[-1]]
            return True

        if word[-1] in current_node.children:
            del current_node.children[word[-1]]
            self.delete_word(word[:-1], depth)
            return True

        return False

if __name__ == '__main__':
    trie = Trie()
    trie.insert_word('stan stem standard money')

    print(trie)

    trie = Trie()

    trie.insert_word('good gerald gold')

    print(trie.search_with_prefix('g'))

    trie.delete_word('gold')
    print(trie.search_with_prefix('g'))