import psycopg2 as db

def getPassword(login):

    con = db.connect(host = "195.150.230.208", port = 5432, database = "2022_nazwisko_imie", user = "2022_nazwisko_imie", password = "*****")


    cursor = con.cursor()
    cursor.execute("SELECT password FROM login2fa.user WHERE login = %s",(login,))
    resultset = cursor.fetchall()
    con.close()
    if len(resultset)>0:
        return resultset[0][0]
    else:
        return False

def userExist(login):
    con = db.connect(host = "195.150.230.208", port = 5432, database = "2022_nazwisko_imie", user = "2022_nazwisko_imie", password = "*****")

    cursor = con.cursor()
    cursor.execute("SELECT * FROM login2fa.user WHERE login = %s", (login,))
    resultset = cursor.fetchall()
    con.close()
    if len(resultset) > 0:
        return True
    else:
        return False

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

def getcodes(login):
    id = getUserId(login)
    codes=[]
    con = db.connect(host = "195.150.230.208", port = 5432, database = "2022_nazwisko_imie", user = "2022_nazwisko_imie", password = "*****")


    cursor = con.cursor()
    cursor.execute("SELECT code FROM login2fa.verify_code WHERE user_id = %s", (id,))
    queryResult = cursor.fetchall()
    con.close()
    for x in queryResult:
        codes.append(x[0])
    return codes

def deleteCode(login,hashcode):
    id = getUserId(login)
    con = db.connect(host = "195.150.230.208", port = 5432, database = "2022_nazwisko_imie", user = "2022_nazwisko_imie", password = "*****")

    cursor = con.cursor()
    cursor.execute("Delete from login2fa.verify_code where user_id=%s and code=%s",(id,hashcode))
    con.commit()
    cursor.close()
    con.close()