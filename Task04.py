# Write a program to create the set {'cat', 1, 2, 3}.
list = ['cat', 1, 2, 3]
print(set(list))

# Write a program to find the length of a set {'c', 'a', 't', '1', '2', '3'}.
set0 = {'c', 'a', 't', '1', '2', '3'}
print(len(set0))

# Write a program to add member(s) in a set.
set1 = {'Blue'}
set2 = {'Green', 'Yellow'}
set2.add('Blue')
print(set2)

# Write a program to remove an item from a set if it is present in the set.
Seta = {0, 1, 2, 3, 4, 5}
for i in Seta:
    if i==4:
        Seta.remove(4)
        break
print(Seta)

# Write a program to find maximum and the minimum value in a set.
set1 = {5, 10, 3, 15, 2, 20}
print('Maximum value from the set is {} '.format(max(set1)))
print('Minimum value from the set is {} '.format(min(set1)))

# Write a program to remove all duplicates from a list using sets.
list = [2, 3, 4, 2, 7, 3, 4, 8, 9, 1, 2, 3]
s = set()
s.update([2, 3, 4, 2, 7, 3, 4, 8, 9, 1, 2, 3])
print(s)
