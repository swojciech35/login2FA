from user import userLogin
from user import userAdd

while True:
    print("\n\n[1]-add new user")
    print("[2]-login user")
    print("[0]-exit")
    operation=input("wybierz operacje:")
    if operation=='1':
        login=input("\n\npodaj login nowego użytkownika: ")
        password=input("podaj hasło: ")
        userAdd(login,password)

    elif operation=='2':
        login=input("podaj login:")
        password= input("podaj haslo:")

        userLogin(login,password)
    elif operation=='0':
        break
