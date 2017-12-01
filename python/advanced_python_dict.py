PLACE YOUR CODE HERE

Q6:
import csv
reader = csv.reader(open('faculty.csv'))
result = {}
for row in reader:
    name = row[0]
    full = name.partition(" ")
    last = full[-1]
    first = full[0]
    if "." in last:
        middle = last[0]
        last = name[3:]
    result[last] = row[1:]
        
        
        
Q7:
  
import csv
reader = csv.reader(open('faculty.csv'))
result = {}
for row in reader:
    name = row[0]
    full = name.partition(" ")
    last = full[-1]
    first = full[0]
    if "." in last:
        middle = last[0]
        last = name[3:]
    result[last,first] = row[1:]
