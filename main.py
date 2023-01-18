from user import userLogin

while True:
    print("\n\npodaj login:")
    login=input()

    print("podaj haslo:")
    password= input()

    userLogin(login,password)
