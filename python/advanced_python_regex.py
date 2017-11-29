Q1:
def Faculty_degrees():
    import pandas as pd
    df2 = pd.read_csv('faculty.csv', delimiter=',')
    print(df2[' degree'].value_counts())
Q2:
def Faculty_titles():
    import pandas as pd
    df2 = pd.read_csv('faculty.csv', delimiter=',')
    print(df2[' title'].value_counts())
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
