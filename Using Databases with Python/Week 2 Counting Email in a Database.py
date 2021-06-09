import sqlite3

conn = sqlite3.connect("emaildb.sqlite")
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Counts''')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

data = open("mbox.txt")
for i in data:
    if not i.startswith("From: "):
        continue
    domain = i.split()[1].split("@")[1]
    #cur.execute('''INSERT INTO Counts (org, count) VALUES (?,1)''', (email,))
    cur.execute('''SELECT count
                    FROM Counts
                    WHERE org = ?''', (domain,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?,1)''',(domain,))
    else:
        cur.execute('''UPDATE Counts
                        SET count = count +1
                        WHERE org = ?''', (domain,))
conn.commit()

sqlstr = '''SELECT org, count
            FROM Counts
            ORDER BY count DESC'''
for i in cur.execute(sqlstr):
    print(i[0],i[1])

cur.close()
