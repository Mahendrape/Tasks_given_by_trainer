# Write a program that uses list and range to create the list [3,6,9,...,99].
L = []
for num in range(3, 100):
    if num % 3 == 0:
        L.append(num)
print(L)

# Write a program to convert a list of characters into single string.
l = ['a', 'b', 'c', 'd']
print(''.join(l))

# Write a program to read a string from the user and print the list of characters in the string.
string = input('Enter the string by the user ')
print(list(string))

# Write a Python program to find the common items from two lists.
color1 = ['Red', 'Green', 'Orange', 'White']
color2 = ['Black', 'Green', 'White', 'Pink']
print(list(set(color1).intersection(set(color2))))

# Write a Python program to get the difference between the two lists.
list1 = [1, 2, 3, 4]
list2 = [1, 2]
print(list(set(list1).difference(set(list2))))

from functools import reduce
#  Write a Python program to get the largest number from a list.
list01 = [1, 2, -8, -2, 0]
print(max(list01))

#  Write a Python program to find the second smallest number from a list.
list00 = [1, 2, -8, -2, 0]
for num in list00:
    if num == -2:
        print(num)
# Another Method
print(num for num in list00 if num == -2)

#  Write a Python program to remove dulipcates from a list.
list0 = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
x = set(list0)
print(list(x))
# Another Method
print([num for num in set(list0)])

#  Write a Python program to sum all the items in a list.
list = [1, 2, -8]
print(sum(list))
# Another Method
print(reduce(lambda a, b: a + b, list))

#  Write a Python program to multiply all the items in a list.
list = [1, 2, 3, 4]
print(reduce(lambda a, b: a * b, list))

#  Write a program to find the difference between sum of even indexed and odd indexed numbers in a list of numbers.
list1 = [2, 4, 3, 9, 13, 12, 7, 6, 1, 5]
a = sum(list1[0::2])
b = sum(list1[1::2])
print(a - b)
# Another Method
print(reduce(lambda a, b: a - b, list1))

# Write a program to print the list of numbers which are greater than the average of numbers in the following list.
list1 = [2, 4, 3, 9, 13, 12, 7, 6, 1, 5]
L = []
for num in list1:
    if num > ((sum(list1)) / num):
        L.append(num)
print(L)
# Another Method
print(["Number is {} ".format(num) for num in list1 if num > ((sum(list1)) / len(list1))])

# Write a program to print a new list containing squares of each element in the following list.
list1 = [3, 7, 11, 12, 17, 21]
L = []
for i in list1:
    L.append(i ** 2)
print(L)
# Another Method
print([a ** 2 for a in list1])

# Write a program to know how many times an element occured in the list.
list1 = [5, 10, 15, 20, 25, 50, 20]
for i in list1:
    print('{} occured {} times '.format(i, list1.count(i)))

# Write a program to find the value 20 in the list, and if it if present, replace the first occurrence of a value with 200.
list1 = [5, 10, 15, 20, 25, 50, 20]
index = list1.index(20)
list1[index] = 200
print(list1)

# Write a program to remove the element at index 4 and add it to the 2nd position and also, at the end of the list.
lis = [54, 44, 27, 79, 91, 41]
lis.remove(91)
lis.insert(2, 91)
lis.append(91)
print(lis)

# Write a program to create a third list by picking an odd-index element from the first list and even index elements from second.
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
list3 = []
a = list1[1::2]
b = list2[0::2]
list3.extend(a)
list3.extend(b)
print(list3)

# Write a program to add 7000 after 6000 in the following list.
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)
