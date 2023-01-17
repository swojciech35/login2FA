from databaseconnect import insertUser
from security import hashPassword
from databaseconnect import getPassword
from security import verifyPassword
def userAdd(login,password):
    passwordEncrypt=hashPassword(password) #szyfrowanie hasła
    insertUser(login,passwordEncrypt)


def userLogin(login,password):
    passwordEnctypted=getPassword(login)
    verify=verifyPassword(password,passwordEnctypted)
    if verify:
        print("zalogowano")
    else:
        print("blad logowania")
