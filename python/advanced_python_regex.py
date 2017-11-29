Q1:
def Degrees():
    import csv
    with open('faculty.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        degrees = []
        for row in reader:
            from collections import Counter
            if row[1] not in degrees: 
                degrees.append(row[1][1:])
        print((Counter(degrees)))
Q2:
def Titles():
    import csv
    with open('faculty.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        titles = []
        for row in reader:
            from collections import Counter
            if row[2] not in degrees: 
                titles.append(row[2][1:])
        print((Counter(titles)))
Q3:
def email_list():
    import csv
    with open('faculty.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        email = []
        for row in reader:
            from collections import Counter
            if row[2] not in email: 
                email.append(row[3])
        print(email)
 Q4
def domains():
    import csv
    with open('faculty.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        email = []
        lst = []
        answer = []
        for row in reader:
            from collections import Counter
            if row[2] not in email: 
                email.append(row[3])
                for x in email:
                    if x not in answer:
                        lst.append(x)
            answer.append(str(lst[-1]).rsplit('@',1)[-1])
    print(list(set(answer)))
