#4.	Write a Python script that takes a list of integers and returns a dictionary whose keys are the list integers and whose values are "even" or "odd" depending on the number parity.
numbers = [1, 4, 6, 7, 8, 19, 22]
odd_even = {}
for number in numbers:
    if number % 2 == 0:
        odd_even[number] = 'even'
    else:
        odd_even[number] = 'odd'
print(odd_even)