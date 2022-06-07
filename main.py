import datetime
from time import strftime

import mysql.connector
from MySQLdb import converters

conv = converters.conversions.copy()
conv[246]=float
conv[10] = str

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="***",
    database="menagerie",
    # conv=conv
)

mycursor = db.cursor(buffered=True)

# mycursor.execute("CREATE DATABASE menagerie")
# mycursor.execute("Use menagerie")

# mycursor.execute("CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), birth DATE, death DATE)")
# mycursor.execute("SHOW TABLES")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)


# mycursor.execute("INSERT INTO pet (name, owner, species, sex, birth) VALUES (%s,%s,%s,%s,%s)", ("Fluffy", "Harold", "cat", "f", "1993-02-04"))
# mycursor.execute("INSERT INTO pet (name, owner, species, sex, birth) VALUES (%s,%s,%s,%s,%s)", ("Claws", "Gwen", "cat", "m", "1994-03-17"))
# mycursor.execute("INSERT INTO pet (name, owner, species, sex, birth) VALUES (%s,%s,%s,%s,%s)", ("Buffy", "Harold", "dog", "f", "1989-05-13"))
# mycursor.execute("INSERT INTO pet (name, owner, species, sex, birth) VALUES (%s,%s,%s,%s,%s)", ("Fang", "Benny", "dog", "m", "1990-08-27"))
# mycursor.execute("INSERT INTO pet (name, owner, species, sex, birth, death) VALUES (%s,%s,%s,%s,%s,%s)", ("Bowser", "Diane", "dog", "m", "1979-08-31", "1995-07-29"))
# mycursor.execute("INSERT INTO pet (name, owner, species, sex, birth) VALUES (%s,%s,%s,%s,%s)", ("Chirpy", "Gwen", "bird", "f", "1998-09-11"))
# mycursor.execute("INSERT INTO pet (name, owner, species, sex, birth) VALUES (%s,%s,%s,%s,%s)", ("Whistler", "Gwen", "bird", "", "1997-12-09"))
# mycursor.execute("INSERT INTO pet (name, owner, species, sex, birth) VALUES (%s,%s,%s,%s,%s)", ("Slim", "Benny", "snake", "m", "1996-04-29"))
# db.commit()

mycursor.execute("SELECT name, owner, species,sex,CAST(birth AS CHAR),CAST( death AS CHAR) FROM pet where sex ='f'")

# mycursor.execute("SELECT * FROM pet WHERE sex ='f'")

# mycursor.execute("SELECT name,CAST(birth AS CHAR) FROM pet")

# mycursor.execute("SELECT * FROM pet ORDER BY name")

# mycursor.execute("SELECT owner, COUNT(species) FROM pet GROUP BY owner HAVING COUNT(species) > 1")

# mycursor.execute("SELECT name, CAST(birth AS CHAR), MONTH(birth) FROM pet")

# mycursor.execute("SHOW DATABASES")

mycursor.execute("SHOW tables")

# mycursor.execute("DELETE FROM pet WHERE name = 'Gwen'")
# db.commit()
# mycursor.execute("show tables")
# mycursor.execute("DROP Table person")
# mycursor.execute("SHOW DATABASES")

myresult = mycursor.fetchall()
for x in myresult:
    # if (type(x) is datetime.date ):
    #     print(strftime(x))
    print(str(x))

