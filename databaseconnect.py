import psycopg2 as db

def getPassword(login):

    con = db.connect(host = "195.150.230.208", port = 5432, database = "2022_nazwisko_imie", user = "2022_nazwisko_imie", password = "*****")


    cursor = con.cursor()
    cursor.execute("SELECT password FROM login2fa.user WHERE login = %s",(login,))
    resultset = cursor.fetchall()
    con.close()
    return resultset[0][0]

def insertUser(login, password):
    con = db.connect(host="195.150.230.208", port=5432, database="2022_nazwisko_imie", user="2022_nazwisko_imie",password="*****")


    cursor = con.cursor()
    cursor.execute("INSERT INTO login2fa.user (login, password) VALUES(%s, %s)", (login,password))
    con.commit()
    cursor.close()
    con.close()

def getUserId(login):

    con = db.connect(host = "195.150.230.208", port = 5432, database = "2022_nazwisko_imie", user = "2022_nazwisko_imie", password = "*****")


    cursor = con.cursor()
    cursor.execute("SELECT id FROM login2fa.user WHERE login = %s",(login,))
    resultset = cursor.fetchall()
    con.close()
    return resultset[0][0]

def insertCodes(login, codes):
    id = getUserId(login)

    con = db.connect(host="195.150.230.208", port=5432, database="2022_nazwisko_imie", user="2022_nazwisko_imie",password="*****")

    for x in codes:
        cursor = con.cursor()
        cursor.execute("INSERT INTO login2fa.verify_code (user_id,code)\
                                        VALUES(%s,%s)",
                        (id,x))
        con.commit()
        cursor.close()
    con.close()