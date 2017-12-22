PLACE YOUR CODE HERE
email = []
def email_list():
    import csv
    with open('faculty.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            from collections import Counter
            if row[2] not in email: 
                email.append(row[3])
        print(email)
        
    with open("emails.csv",'w') as resultFile:
        wr = csv.writer(resultFile)
        wr.writerow(email)
