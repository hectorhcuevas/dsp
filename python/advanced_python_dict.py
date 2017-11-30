PLACE YOUR CODE HERE

Q6:
  with open('faculty.csv', mode='r') as infile:
    reader = csv.reader(infile)
    name = []
    for rows in reader:
        name = rows[0].partition(" ")
        #print(name)
        last = (name[-1])
        first = (name[0])
        v = rows[1:]
        if "." in last:
            Middle_initial = last[0]
            last = last[3:]
        for x in name:
            mydict = {last:v}
        print(mydict)
        
        
        
Q7:
  
  with open('faculty.csv', mode='r') as infile:
    reader = csv.reader(infile)
    name = []
    for rows in reader:
        name = rows[0].partition(" ")
        #print(name)
        last = (name[-1])
        first = (name[0])
        v = rows[1:]
        if "." in last:
            Middle_initial = last[0]
            last = last[3:]
        for x in name:
            mydict = {first,last:v}
        print(mydict)
