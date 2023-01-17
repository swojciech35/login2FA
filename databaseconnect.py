import psycopg2 as db

def queryDatabase(query):

    con = db.connect(host = "195.150.230.208", port = 5432, database = "2022_nazwisko_imie", user = "2022_nazwisko_imie", password = "*****")


    cursor = con.cursor()
    cursor.execute(query)
    resultset = cursor.fetchall()
    con.close()
    return resultset

def insertUser(login, password):
    con = db.connect(host="195.150.230.208", port=5432, database="2022_nazwisko_imie", user="2022_nazwisko_imie",password="*****")

    cursor = con.cursor()
    cursor.execute("INSERT INTO login2fa.user (login, password) VALUES(%s, %s)", (login,password))
    con.commit()
    cursor.close()
    con.close()
