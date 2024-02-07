# newList = [ expression(element) for element in oldList if condition ] 
# Python List comprehension provides a much more short syntax for creating a new list based on the values of an existing list.

# Example1)using python
# Using list comprehension to iterate through loop
List = [character for character in [1, 2, 3]]
# Displaying list
print(List)

"""Even list using list comprehension"""
list1=[i for i in range(11) if i%2==0]
print(list1)

"""Matrix using List comprehension"""
matrix=[[j for j in range(3)] for i in range(3)]
print(matrix)

"""List Comprehensions vs For Loop"""
List=[]
for character in 'Geeks for Geeks':
    List.append(character)
print(List)

# using lambda to print table of 10
# numbers = list(map(lambda i: i*10, [i for i in range(1, 6)]))
# print(numbers)

"""using lambda and map"""
List1=[2,4]
List2=[6,7]
multiplay_of_two_list=list(map(lambda x, y: x * y, List1,List2))
print("multiplay_of_two_list =",multiplay_of_two_list)

"""Add in lambda here z is var"""
z=lambda x:x*2
print(z(2))

"""Conditionals in List Comprehension"""
List=["Even Number" if i%2==0 else "Odd Number" for i in range(8)]
print(List)

"""Nested IF with List Comprehension"""
lis = [num for num in range(100)
	if num % 5 == 0 if num % 10 == 0]
print(lis)


