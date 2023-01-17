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


    cursor = con.cursor()
    cursor.execute("INSERT INTO login2fa.code (user_id, code1,code2,code3,code4,code5,code6,code7,code8,code9,code10,\
                                                        code11,code12,code13,code14,code15,code16,code17,code18,code19,\
                                                        code20,code21,code22,code23,code24,code25,code26,code27,code28,\
                                                        code29,code30)\
                                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                                           %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (id,codes[0],codes[1],codes[2],codes[3],codes[4],codes[5],codes[6],codes[7],codes[8],codes[9],codes[10],
                        codes[11],codes[12],codes[13],codes[14],codes[15],codes[16],codes[17],codes[18],codes[19],codes[20],
                        codes[21],codes[22],codes[23],codes[24],codes[25],codes[26],codes[27],codes[28],codes[29]))
    con.commit()
    cursor.close()
    con.close()