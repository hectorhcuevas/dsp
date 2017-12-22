PLACE YOUR CODE HERE

Q6:
import csv
reader = csv.reader(open('faculty.csv'))
result = {}
for row in reader:
    name = row[0]
    full = name.split()
    last = full[-1]
    first = full[0]
    result[last] = row[1:]
print(result)
        
        
        
Q7:
  
import csv
reader = csv.reader(open('faculty.csv'))
result = {}
for row in reader:
    name = row[0]
    full = name.split()
    last = full[-1]
    first = full[0]
    result[last,first] = row[1:]
print(result)
