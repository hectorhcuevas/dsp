Q1:
def Faculty_degrees():
    import pandas as pd
    df2 = pd.read_csv('faculty.csv', delimiter=',')
    print(df2[' degree'].value_counts())
Q2:
def email_list():
    import pandas as pd
    df2 = pd.read_csv('faculty.csv', delimiter=',')
    lst = []
    for email in df2[' email']:
        if email not in lst:
            lst.append(email)
            print(lst[-1])
    
