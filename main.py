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

This solution ensures data immutability because it does not modify the original input array. 
Instead, it creates a new list arr and appends each element from array to it. 
The sorting operation is also performed on the new list, leaving the original input unchanged.


2. How does this solution ensure data immutability?

Yes, this solution is a pure function because it does not have any side effects and always returns the same output given the same input.


3. Is this solution a pure function? Why or why not?

No, this solution is not a higher-order function because it does not take any functions as arguments or return any functions as output.


4. Is this solution a higher order function? Why or why not?




5. Would it have been easier to solve this problem using a different programming style?
Why in particular is functional programming a helpful paradigm when solving this problem?
"""