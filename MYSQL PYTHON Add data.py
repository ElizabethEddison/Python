import mysql.connector

mydb = mysql.connector.connect(
    user = "root",
    password = "Rootjhgs21",
    database="videogames"
)

mycursor = mydb.cursor()

def addgame():
    gamename = input("Please enter game name")
    genre = input("Please enter the genre")
    rating = input("Please enter ratings")

    sql = "INSERT INTO games (gamename, genre, rating) VALUES (%s, %s, %s)"
    val = (gamename, genre, rating)

    mycursor.execute(sql, val)

    mydb.commit()

def viewgames():
    query = "SELECT * FROM games"

    mycursor.execute(query)

    records = mycursor.fetchall()
    for record in records:
        print(record)

selection = input("Please enter selection \n 1. Add game\n2. View Games")
if selection == "1":
    addgame()
elif selection == "2":
    viewgames()
