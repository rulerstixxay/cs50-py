from sys import argv, exit
import cs50


#Command Line arg
if len(argv) != 2:
    print("usage: roster.py (House)")
    exit(1)

print(argv[1])
#Open students.db in SQLite
db = cs50.SQL("sqlite:///students.db")

#Use with SQL query
rows = db.execute("SELECT * FROM students WHERE house=? ORDER BY last ASC, first ASC", argv[1])
for x in rows:
    if x["middle"] != None:
        print(f"{x['first']} {x['middle']} {x['last']}, born {x['birth']}")
    else:
        print(f"{x['first']} {x['last']}, born {x['birth']}")

