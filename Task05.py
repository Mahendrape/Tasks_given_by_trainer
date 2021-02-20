# Write a program to prompt the user to give name and marks of 5 different students,
# store them in dictionary and print it after sorting the dictionary with respect to their marks.
students = {'Madhu': 540,
            'Vishnu': 500,
            'Chandhana': 530,
            'Mahendra': 490,
            'Prasad': 525
            }
x = sorted(students.values())
print(x)

# Use the dictionary given below whose keys are month names and whose values are the number of days in the corresponding months.
# (a) Ask the user to enter a month name and use the dictionary to tell them how many days are in the month.
days = {' January ': 31, ' February ': 28, ' March ': 31, ' April ': 30,
        ' May': 31, ' June ': 30, ' July ': 31, ' August ': 31,
        ' September ': 30, ' October ': 31, ' November ': 30, ' December ': 31}
i = input('Enter the month name  ')
for x in days:
    if x.strip() == i:
        print(days[x])

# (b) Print out all of the keys in alphabetical order.
x = sorted(days.keys())
print(x)

# (c) Print out all of the months with 31 days.
for (k, v) in days.items():
    if v == 31:
        print(k)

# Write a program to count the number of characters (character frequency) in a string.
string = 'google'
d = {}
for chr in string:
    count = 0
    for m in string:
        if m == chr:
            count += 1
    d[chr] = count
print(d)

# Write a program to count the number of occurrences of each letter in word "MISSISSIPPI".
# Store count of every letter with the letter in a dictionary and print the sorted dictionary according to the count of letters.
string = 'MISSISSIPPI'
d = {}
for chr in string:
    count = 0
    for m in string:
        if m == chr:
            count += 1
    d[chr] = count
print(d)
print(sorted(d.values()))

# Write a program to count the occurrences of each word in the text given below.
Text = 'Through three cheese trees three free fleas flew While these fleas flew freezy breeze blew Freezy breeze made these three trees freeze Freezy trees made these trees cheese freeze Thats what made these three free fleas sneeze'
l = Text.split()
# print(l)
# print(len(l))
# n = len(l) - 1
# print(n)
d = {}
for word in l:
    count = 0
    for w in l:
        if w == word:
            count += 1
    d[word] = count
print(d)

# Write a program to get the frequency of the elements in a list.
list = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
dic = {}
for num in list:
    count = 0
    for m in list:
        if m == num:
            count += 1
    dic[num] = count
print(dic)

# Write a program to concatenate following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {**dic1, **dic2, **dic3}
print(dic4)

# Write a program to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
d = {}
for i in range(1, 15):
    d[i] = i ** 2
print(d)
# Another Method
print({i: i ** 2 for i in range(1, 16)})

# Write a Python program to print the sum all the values in a dictionary.
dict = {'data1': 100, 'data2': 54, 'data3': 247}
print(sum(dict.values()))

# Write a program that reads through any dictionary given below and prints the following:
d = [
    {' name ': ' Todd ', ' phone ': ' 555-1414 ', ' email ': ' todd@mail.net '},
    {' name ': ' Helga ', ' phone ': ' 555-1618 ', ' email ': ' helga@mail.net '},
    {' name ': ' Princess ', ' phone ': ' 555-3141 ', ' email ': ''},
    {' name ': ' LJ ', ' phone ': ' 555-2718 ', ' email ': ' lj@mail.net '}
]
# (a) All the users whose phone number ends in an 8
for i in d:
    p = i.get(' phone ').strip(' ')
    if p.endswith('8'):
        print(p)

# (b) All the users that don’t have an email address listed
for i in d:
    e = i.get(' email ').strip(' ')
    if e == '':
        print(e)
        print('Successfully executed')
