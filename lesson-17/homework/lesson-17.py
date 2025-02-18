import sqlite3

connection = sqlite3.connect('hometask-17.sqlite')

cursor = connection.cursor()

create_table = "create table if not exists Roster(Name text, Species text, Age int)"

insert_values = "Insert into Roster values ('Benjamin Sisko', 'Human', 40), ('Jadzia Dax', 'Trill', 300), ('Kira Nerys', 'Bajoran', 29)"

update_values="Update Roster set name='Ezri Dax' where name='Jadzia Dax'"

display="select name, age from Roster where species='Bajoran'"

cursor.execute(create_table)

cursor.execute(insert_values)

cursor.execute(update_values)

cursor.execute(display)

# cursor.execute("select * from Roster")

#cursor.execute("Drop table Roster")

results=cursor.fetchall()

for result in results:
    print(result)

connection.commit()

connection.close()