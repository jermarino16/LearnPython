import sqlite3

conn = sqlite3.connect("my_friends.db")

#create cursor object
c = conn.cursor()

#do some sql
# c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER)")

insert_query = '''INSERT INTO friends
					VALUES ('Merriwehter', 'Lewis', 7)'''

# form_first = "mary-todd"
# query = f"INSERT INTO friends (first_name) VALUES (?)"
# c.execute(query, (form_first,))

# data = ("steve", "irwin", 9)
# query = "INSERT INTO friends VALUES (?,?,?)"
# c.execute(query, data)

#do many functions
people = [
	("Jeremy", "Marino", 5),
	("Bubs", "Marino", 5),
	("Erica", "Marino", 5)
]

# for person in people: # one way to insert a lot
# 	c.execute("INSERT INTO friends VALUES (?,?,?)", person)
# 	print("Inserted yo")

# c.executemany("INSERT INTO friends VALUES(?,?,?)", people) # another way

#commit changes
conn.commit()
conn.close()