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

It might have been easier to solve this problem using a different programming style, such as using list comprehensions or recursion. 
However, the solution presented here is clear and readable, and it effectively solves the problem.


5. Would it have been easier to solve this problem using a different programming style?
Why in particular is functional programming a helpful paradigm when solving this problem?

Functional programming is helpful when solving this problem because it emphasizes immutability and avoids side effects. 
The solution presented here creates a new list instead of modifying the original input, and it does not have any side effects. 
This makes the code easier to reason about and more robust. Additionally, the use of functions like `append` and `sorted` allows us to 
break down the problem into smaller, composable pieces, which is a key concept in functional programming.

"""

#OOP
#Watto needs a new system for organizing his inventory of podracers. 
#Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes. 
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
  
  def boost(self):
    self.max_speed *= 2
    
# Define another class that inherits Podracer and call this one SebulbasPod. 
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
  
  def flame_jet(self,other):
    other.condition = "trashed"

"""
Make sure to answer the following prompts about your coding experience:

How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)

Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?

How in particular did Object Oriented Programming assist in the solving of this problem?

"""