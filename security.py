import argon2

ph = argon2.PasswordHasher()

def hashPassword(password):
    ph = argon2.PasswordHasher(time_cost=32, memory_cost=2 ** 15, parallelism=4, hash_len=64, salt_len=32,
                               encoding="utf-8", type=argon2.Type.ID)
    return ph.hash(password)

def verifyPassword(password,hash):
    try:
        ph.verify(hash, password)
        return True
    except argon2.exceptions.VerifyMismatchError as e:
        print(e)
    return False