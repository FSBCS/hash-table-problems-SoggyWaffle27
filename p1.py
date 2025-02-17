# '''
# Given a list of strings, group the strings into lists of anagrams.
# Return the groups as a list of lists. 
# For example, if the input is: ["bat", "meta", "tab", "tea", "ate", "tame", "jazz", "eat"],
# the output would be: [["bat", "tab"], ["meta", "tame"], ["tea", "ate", "eat"],["jazz"]]

# If three words are anagrams, what common key could we store to represent them in a hash table?

# To convert a list to a string, we can use `''.join(someList)` 
# to concatenate the elements of the list to the empty string.
# '''


# def hash(string):
#     letters = {
#         'a': 65, 'b': 66, 'c': 67, 'd': 68, 'e': 69, 'f': 70, 'g': 71, 'h': 72, 'i': 73, 'j': 74,
#         'k': 75, 'l': 76, 'm': 77, 'n': 78, 'o': 79, 'p': 80, 'q': 81, 'r': 82, 's': 83, 't': 84,
#         'u': 85, 'v': 86, 'w': 87, 'x': 88, 'y': 89, 'z': 90
#     }
#     hash = 0
#     for i in string.lower():
#         if i == ' ':
#             pass
#         else:   
#             hash += letters[i]
#     return hash % 100

# def group_anagrams(words =  ["bat", "meta", "tab", "tea", "ate", "tame", "jazz", "eat", "phetenal", "elephant"]):
#     grams = {}
#     for i in words:
#         if hash(i) in grams:
#             grams[hash(i)].append(i)
#         else:
#             grams[hash(i)] = [i]
#     out = []
#     for i in grams:
#         out.append(grams[i])
#     return out


# group_anagrams()

def group_anagrams(words =  ["bat", "meta", "tab", "tea", "ate", "tame", "jazz", "eat", "phetenal", "elephant"]):
    table = {}
    for word in words:
        sort = []
        for i in word:
            sort.append(i)
        sort = sorted(sort)
        out = ""
        for i in sort:
            out += i
        if out in table:
            table[out].append(word)
        else:
            table[out] = [word]
    output = []
    for i in table:
        output.append(table[i])
    return output
print(group_anagrams())