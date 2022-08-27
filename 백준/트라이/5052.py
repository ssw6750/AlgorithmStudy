from collections import defaultdict
from sys import stdin

input = stdin.readline


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.cnt = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.total_cnt = 0
        self.flag = 'YES'

    def insert_word(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
            if node.cnt != 0:
                print("asass")
                self.flag = 'NO'
                return                
        node.cnt += 1
        self.total_cnt += 1

    def show_flag(self) -> None:
        print(self.flag)


def main():
    for _ in range(int(input())):
        trie = Trie()
        n = int(input())
        for i in range(n):
            tmp = input()
            trie.insert_word(tmp[:-1])

        trie.show_flag()


if __name__ == "__main__":
    main()