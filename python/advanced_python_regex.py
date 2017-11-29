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
    import pandas as pd
    df2 = pd.read_csv('faculty.csv', delimiter=',')
    lst = []
    for x in list(df2[' email']):
        if x not in lst:
            lst.append(x)
    print(lst)
 Q4
def Domains():
    import pandas as pd
    df2 = pd.read_csv('faculty.csv', delimiter=',')
    mail = df2[' email']
    lst = []
    answer = []
    for x in mail:
        if x not in lst:
            lst.append(x)
            answer.append(str(lst[-1]).rsplit('@',1)[-1])
    print(list(set(answer)))
