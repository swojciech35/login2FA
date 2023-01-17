from databaseconnect import insertUser
from security import hashPassword


def userAdd(login,password):
    passwordEncrypt=hashPassword(password) #szyfrowanie hasła
    insertUser(login,passwordEncrypt)


