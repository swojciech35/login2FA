from databaseconnect import insertUser
from security import hashPassword
from databaseconnect import getPassword
from security import verifyPassword
from databaseconnect import getcodes
from security import verifyCode
from databaseconnect import insertCodes
from security import generateCodes
from security import hashCodes


def userAdd(login,password):
    passwordEncrypt=hashPassword(password) #szyfrowanie hasła
    insertUser(login,passwordEncrypt)
    insertCodes(login,hashCodes(generateCodes()))
    print("Dodano nowego użytkownika")
def userLogin(login,password):
    passwordEnctypted=getPassword(login)
    if passwordEnctypted !=False:
        verify=verifyPassword(password,passwordEnctypted)
        if verify:
            login2fa(login)
        else:
            print("błędne hasło")
    else:
        print("podaj poprawne dane logowania")
def login2fa(login):
    code=input("podaj kod weryfikacyjny:")
    codes= getcodes(login)
    ver=verifyCode(code,codes)
    if ver:
        print("zalogowano")
    else:
        print("bledny kod weryfikacyjny")