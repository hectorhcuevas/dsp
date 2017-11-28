def Faculty_degrees():
    import pandas as pd
    df2 = pd.read_csv('faculty.csv', delimiter=',')
    print(df2[' degree'].value_counts())
    
