# time: O(n)
# space: O(26^max(w_length))
class TrieNode:
    def __init__(self):
        self.containingLetters = {}

    def containLetter(self, letter):
        return letter in self.containingLetters
    
    def getNextTrieNode(self, letter):
        return self.containingLetters.get(letter, None)

    def setLetter(self, letter):
        self.containingLetters[letter] = TrieNode()

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if curr.containLetter(char):
                curr = curr.getNextTrieNode(char)
            else:
                curr.setLetter(char)
                curr = curr.getNextTrieNode(char)
        curr.setLetter('#') 

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if curr.containLetter(char):
                curr = curr.getNextTrieNode(char)
            else:
                return False
        return curr.containLetter('#')

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if curr.containLetter(char):
                curr = curr.getNextTrieNode(char)
            else:
                return False
        return True