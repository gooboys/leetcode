'''
208. Implement Trie (Prefix Tree)

Difficulty: Medium
Topics: Trie, Design, Tree
Companies: Common in technical interviews

Problem Description:
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. 
It has various applications such as autocomplete and spellchecker.

Task:
Implement the `Trie` class:
1. `Trie()`: Initializes the trie object.
2. `void insert(String word)`: Inserts the string `word` into the trie.
3. `boolean search(String word)`: Returns `True` if the string `word` is in the trie (i.e., it was inserted before), and `False` otherwise.
4. `boolean startsWith(String prefix)`: Returns `True` if there is a previously inserted string `word` that has the prefix `prefix`, and `False` otherwise.

Examples:

Example 1:
Input:
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output:
[null, null, true, false, true, null, true]

Explanation:
Trie trie = new Trie();
trie.insert("apple");         # Insert "apple" into the trie
trie.search("apple");         # Returns True (exact match found)
trie.search("app");           # Returns False (no exact match for "app")
trie.startsWith("app");       # Returns True (a word starts with "app")
trie.insert("app");           # Insert "app" into the trie
trie.search("app");           # Returns True (now "app" exists in the trie)

Constraints:
1. 1 <= word.length, prefix.length <= 2000
2. `word` and `prefix` consist only of lowercase English letters.
3. At most 3 * 10^4 calls in total will be made to `insert`, `search`, and `startsWith`.
'''


class Trie(object):

    def __init__(self):
        self.tracker = {}
        self.pref = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.tracker[word] = 1
        ret = ""
        for char in word:
            ret = ret+char
            self.pref[ret] = 1
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        track = self.tracker.get(word,0)
        if track:
            return True
        else:
            return False


    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        track = self.pref.get(prefix,0)
        if track:
            return True
        else:
            return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)