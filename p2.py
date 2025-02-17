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
    #[(elements[x], x) for x in elements.keys()]
    o.sort()
    print(o)
    while k != 0:
        p = o.pop()
        if p[1] != o[-1]:
            k -= 1
        out.append(p[1])
    return out

def k_most_frequent(lst, k):
    if k > len(lst):
        return lst
    dict = {}
    for element in lst:
        dict[element] = dict.get(element, 0) + 1
    dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse = True)}
    output, number  = [], []
    for i in dict:
        if len(number) != 0 and number[-1] != dict[i]:
            k -= 1
        output.append(i)
        number.append(dict[i])
        print(output, number, k)
        if k == 1: 
            return output
    return output
    


print(k_most_frequent([1, 1, 2, 2, 1, 3], 2))