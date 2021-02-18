# Write a program to insert a new element into tuple of elements at a specified position.
x = (1, 2, 3, 4)
y = list(x)
y.insert(2, 'Mahi')
print(tuple(y))

# Write a program to count the number of even and odd numbers from a tuple of numbers.
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
x = 0
y = 0
for num in tuple1:
    if num % 2 == 0:
        x += 1
    else:
        y += 1
print('Number of even numbers: {} '.format(x))
print('Number of odd numbers: {} '.format(y))

# Write a program to modify or replace an existing element of a tuple with a new element.
x = (1, 2, 3, 4)
y = list(x)
n = 2
y[1:n] = [10]
print(tuple(y))

# Write a program to find Dissimilar Elements in Tuples.
tuple1 = (3, 4, 5, 6)
tuple2 = (5, 7, 4, 10)
print('Dissimilar elements in tuples are:{} '.format(tuple(set(tuple1).symmetric_difference(set(tuple2)))))

from functools import reduce

# Write a program for addition of tuples.
tuple1 = (10, 4, 5)
tuple2 = (2, 5, 18)
x = list(tuple1)
y = list(tuple2)
print('Addition of tuples is:{} '.format(tuple(map(lambda x, y: x + y, x, y))))

# Write a program to sort the following employ data (list of tuples) as per their salaries (each tuple represents employ ID, name, age and salary)?
data = [(1234, 'Abishek', 32, 35000), (4532, 'Barathi', 27, 29000), (3455, 'Charan', 31, 37000),
        (9863, 'Devi', 42, 52000), (4852, 'Eswar', 37, 56000), (6481, 'Fathima', 40, 65000),
        (2793, 'Ganesh', 28, 45000)]
z = map(lambda a: a[3], data)
y = list(z)
print(y)
y.sort()
print(y)

# Write a program to count the number of students has computers as one subject from the data given below.
students = [("John", ["Computers", "Physics", "Maths"]),
            ("Wasim", ["Maths", "Computers", "Statistics"]),
            ("Naresh", ["Computers", "Accounting", "Economics"]),
            ("SaiTeja", ["English", "Accounting", "Economics", "Law"]),
            ("Sravani", ["Sociology", "Economics", "Law", "Stats", "Music"])]

x = 0
for string in students:
    if string == 'Computers':
        x += 1
        print('Number of students has computers as one subject: {} '.format(x))

