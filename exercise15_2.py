# Counting email organization from a file
# Input it to a database

import sqlite3

# Opening sqlite3
conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

# Creating database
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# File name input
fname = input('Enter file name:')
if len(fname) < 1:
    fname = 'mbox-short.txt'

fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue

    # Parsing organization data from email
    words = line.split()
    email = words[1]
    pieces = email.split('@')
    org = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    row = cur.fetchone()

    # Insert organization count
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                    VALUES (?, 1)''', (org, ))
    else:
        cur.execute('''UPDATE Counts SET count = count + 1
                    WHERE org = ?''', (org, ))

conn.commit()

# Counting organization and sorting it as output in python
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
