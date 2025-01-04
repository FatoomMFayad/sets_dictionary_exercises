#6.	Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list without all the duplicates.
my_list = [1, 2, 3, 2, 4, 5, 3]
new_list = set(my_list)
print(new_list)