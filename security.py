import argon2
import random
import string
ph = argon2.PasswordHasher()

def hashPassword(password):
    ph = argon2.PasswordHasher(time_cost=32, memory_cost=2 ** 15, parallelism=4, hash_len=64, salt_len=32,
                               encoding="utf-8", type=argon2.Type.ID)
    return ph.hash(password)

def verifyPassword(password,hash):
    try:
        ph.verify(hash, password)
        return True
    except:
        None
    return False

def generateCodes():
    source = string.ascii_letters + string.digits
    codes=[]
    for i in range(1,31):
        codes.append( ''.join((random.choice(source) for i in range(5))))
    print("Twoje jednorazowe kody dostępu to:")
    print(codes)
    print("zapisz je w celu zalogowania się do konta")
    return codes

def hashCodes(codes):
    ph = argon2.PasswordHasher(time_cost=32, memory_cost=2 ** 15, parallelism=4, hash_len=64, salt_len=32,
                               encoding="utf-8", type=argon2.Type.ID)
    codesHash=[]
    for i in codes:
        codesHash.append(ph.hash(i))

    return codesHash


def verifyCode(code,codes):
    for i in codes:
        try:
            ph.verify(i,code)
            print("code accept")
            return i
        except:
            None

    return False