from databaseconnect import insertUser
from security import hashPassword
from security import verifyPassword
from user import userAdd
from user import userLogin
from databaseconnect import getUserId
from security import generateCodes
from databaseconnect import insertCodes
from databaseconnect import getcodes
from security import verifyCode
from security import hashCodes
print(hashPassword("test"))
print(hashPassword("test"))
print(verifyPassword("test","$argon2id$v=19$m=32768,t=32,p=4$Do/qGLU0qCEf9Z2m395+SdjIlqlsYJ1LUEj2wog392g$HrqN4dK0uOpJ+WSTMtdRbB0k4IKShPtvPaMIy91lffc5DZnq4kwCYZCVGyX3HTCd+saPrVqFZGSc3MekVDX1Bg"))
print(verifyPassword("test1","$argon2id$v=19$m=32768,t=32,p=4$Do/qGLU0qCEf9Z2m395+SdjIlqlsYJ1LUEj2wog392g$HrqN4dK0uOpJ+WSTMtdRbB0k4IKShPtvPaMIy91lffc5DZnq4kwCYZCVGyX3HTCd+saPrVqFZGSc3MekVDX1Bg"))

# userAdd("user3","password")
userLogin("user3","password")
userLogin("user3","passwordd")
print(getUserId("user2"))
codes=generateCodes()
print(codes[9])
# insertCodes("user3",generateCodes())
print(getcodes("user3"))

# print(hashCodes(generateCodes()))
# insertCodes("user3",hashCodes(generateCodes()))
print(verifyCode("mXKgkk",getcodes("user3")))