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
def Domains():
    import csv
    with open('faculty.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        email = []
        answer = []
        for row in reader:
            from collections import Counter
            if row[2] not in email: 
                email.append(row[3])
            answer.append(str(email[-1]).rsplit('@',1)[-1])
    print(list(set(answer)))
