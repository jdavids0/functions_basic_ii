# 1. Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
from ctypes import sizeof


def countdown(num):
    new_list = []
    for i in range (num, -1, -1):
        new_list.append(i)
    return new_list
        
print(countdown(10))

# 2. Create a function that will receive a list with two numbers. Print the first value and return the second.
def Return(x):
    print(x[0])
    return x[1]

Return([8,12])

# 3. Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def firstPlusLength(x):
    return x[0] + len(x)

print(firstPlusLength([6,14,-4,3]))

# 4. Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False.
def greaterThanSecond(x):
    new_list = []
    for i in range (len (x)):
        if x[i] > x[1]:
            new_list.append(x[i])
    print(len(new_list))
    return new_list

print(greaterThanSecond([3,7,10,-5,12]))

# 5. Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

def thisThat(size, value):
    new_list = []
    for i in range (size):
        new_list.append(value)
    return new_list

print(thisThat(5, 8))