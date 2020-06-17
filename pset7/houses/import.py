import csv
import cs50
from sys import argv, exit

#Command Line arg
if len(argv) != 2:
    print("usage: import.py characters.csv")
    exit(1)

#Open students.db in SQLite
db = cs50.SQL("sqlite:///students.db")
#db.execute("CREATE TABLE students (first TEXT, middle TEXT, last TEXT, house TEXT, birth NUMERIC)")
    #seems like students table already exists (Error i got)

#Open CSV file
with open(argv[1], "r") as file:
    #Create DictReader
    reader = csv.DictReader(file, delimiter=",")
    for row in reader:
        name = row["name"]
        house = row["house"]
        birth = row["birth"]

        #Splitting the name into "first", "middle", "last"
        tem = name.split()
        #if student has middle name
        if len(tem) == 3:
            first = tem[0]
            middle = tem[1]
            last = tem[2]
        #if student has no middle name
        elif len(tem) == 2: #not necessary, can just use else, but trying to be specific
            first = tem[0]
            middle = None
            last = tem[1]

        #time to fill in the SQL table
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
        first, middle, last, house, birth)





