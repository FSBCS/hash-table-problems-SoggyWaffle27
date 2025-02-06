'''
Given a list and a value k, return the k most frequently occurring elements. 
If there is a tie for kth-most frequent, return all the tied elements. 
If k is greater than the number of unique elements, return a list of all the unique elements.
'''


def k_most_frequent(lst, k):
    elements = {}
    o = []
    out = []
    for i in lst:
        if i in elements:
            elements[i] += 1
        else:
            elements[i] = 1
    for i in elements:
        o.append((elements[i], i))
    o.sort()
    print(o)
    while k != 0:
        p = o.pop()
        if p[1] != o[-1]:
            k -= 1
        out.append(p[1])
    return out

print(k_most_frequent([1, 1, 2, 2, 3, 3], 2))