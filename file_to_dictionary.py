#7.	Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen as a dictionary [key is the name, value is the count].
f = open('C:/Users/Fatoom/Documents/names.txt')
names = f.readlines()
names_count = {}
for name in names:
    name = name.strip()
    if name in names_count:
        names_count[name] += 1
    else:
        names_count[name] = 1
print(names_count)