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

1. Abstraction: The classes and methods defined in the solution abstract the complex details of podracers, their properties, and actions from the rest of the code. 
The properties and behaviors are encapsulated within their respective classes, making the code more modular and easier to understand.

2. Inheritance: The solution utilizes inheritance to create a hierarchy of classes, where the child classes (AnakinsPod and SebulbasPod) inherit properties and methods from the parent class (Podracer). 
This helps to reduce code duplication and promotes code reuse.

3. Polymorphism: The solution demonstrates polymorphism through the use of different methods with the same name but different functionality in the child classes (boost and flame_jet). 
These methods operate differently depending on the class they belong to.

4. Encapsulation: The solution encapsulates data and behaviors within their respective classes, preventing them from being accessed or modified in unintended ways. 
The properties of each class can only be accessed or modified through specific methods defined within that class.


Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?

It may have been possible to implement a solution to this problem using a different coding 
style such as procedural or functional programming, but object-oriented programming 
provides a more intuitive and natural way to model entities with complex properties and behaviors.

How in particular did Object Oriented Programming assist in the solving of this problem?

Object-oriented programming assisted in solving this problem by allowing us to create 
classes that represent real-world entities and encapsulate their properties and behaviors. 
The use of inheritance and polymorphism also helped to make the code more modular 
and easier to understand, as well as promoting code reuse. Overall, OOP helped to create 
a more organized and scalable solution to the problem of organizing inventory for podracers.

"""