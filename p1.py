'''
Given a list of strings, group the strings into lists of anagrams.
Return the groups as a list of lists. 
For example, if the input is: ["bat", "meta", "tab", "tea", "ate", "tame", "jazz", "eat"],
the output would be: [["bat", "tab"], ["meta", "tame"], ["tea", "ate", "eat"],["jazz"]]

If three words are anagrams, what common key could we store to represent them in a hash table?

To convert a list to a string, we can use `''.join(someList)` 
to concatenate the elements of the list to the empty string.
'''

def group_anagrams(words =  ["bat", "meta", "tab", "tea", "ate", "tame", "jazz", "eat", "phetenal", "elephant"]):
    table = HashTable()
    for i in words:
        table.insert(i)
    print(table.display())
    print(table.find("tab"))


class HashTable():
    def __init__(self, size=100):
        self.table = [0] * size
    def resize(self):
        new_table = [0] * len(self.table) * 2
        for i in self.table:
            new_table.append(hash(i))
        self.table = new_table
    def display(self):
        return self.table
    def find(self, string):
        hash = self.hash(string)
        while self.table[hash] != string:
            hash += 1
            if hash == self.hash(string):
                self.resize()
            if hash < len(self.table):
                hash == 0
        return hash
    def insert(self, string):
        hash = self.hash(string)
        while True:
            if self.table[hash % 100] == 0:
                break
            else:
                hash += 1
        self.table[hash % 100] = string

    def hash(self, string):
        letters = {
            'a': 65, 'b': 66, 'c': 67, 'd': 68, 'e': 69, 'f': 70, 'g': 71, 'h': 72, 'i': 73, 'j': 74,
            'k': 75, 'l': 76, 'm': 77, 'n': 78, 'o': 79, 'p': 80, 'q': 81, 'r': 82, 's': 83, 't': 84,
            'u': 85, 'v': 86, 'w': 87, 'x': 88, 'y': 89, 'z': 90
        }
        hash = 0
        for i in string.lower():
            if i == ' ':
                pass
            else:   
                hash += letters[i]
        return hash % 100
    

group_anagrams()