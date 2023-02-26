#Functional
#Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

"""
1. Make sure to answer the following questions about your coding process:

2. How does this solution ensure data immutability?

3. Is this solution a pure function? Why or why not?

4. Is this solution a higher order function? Why or why not?

5. Would it have been easier to solve this problem using a different programming style?
Why in particular is functional programming a helpful paradigm when solving this problem?
"""