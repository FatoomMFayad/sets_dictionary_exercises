#3.	Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
#Sample Dictionary ( n = 5) :
#Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
sqaures = {}
for i in range(1, 6, 1):
    sqaures.update({i: i**2})
print(sqaures)
