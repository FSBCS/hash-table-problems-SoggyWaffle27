'''
Given a list of integers and a target sum, return the number of continuous subarrays that sum to sum. 
For example, if the input is [1,1,1] and sum=2, the output should be 2.

1, 1, 1, 2, 1, 2, 1

Believe it or not, it is possible to do this with just one pass through the list! 
In the brute force solution (computing every subarray sum) we end up doing a lot of repeat work,
so our goal should be to calculate the values of subarrays only once.

Here's the strategy. Loop over the elements of the list and:

1. store the `current_sum` (the sum of the first $i$ elements) in a hash table counting how many times that sum has appeared so far.

2. Use the hash table to figure out if there are any subarrays ending at the current element which sum to `k`. Increment a counter if you do.

Finally, return the number of subarrays found.
'''

def count_subarrays_with_sum(arr, sum):
    table = {}
    out = 0
    if arr == []:
        return 0
    for i in range(0, len(arr) + 1):
        if hash(arr[:i]) - sum in table:
            out += table[hash(arr[:i]) - sum]
        if hash(arr[:i]) in table:
            table[hash(arr[:i])] += 1
        else:
            table[hash(arr[:i])] = 1
    return out

def hash(arr):
    return sum(arr)