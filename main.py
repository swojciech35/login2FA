from databaseconnect import insertUser
from security import hashPassword
from security import verifyPassword
from user import userAdd
from user import userLogin
from databaseconnect import getUserId
print(hashPassword("test"))

print(verifyPassword("test","$argon2id$v=19$m=32768,t=32,p=4$Do/qGLU0qCEf9Z2m395+SdjIlqlsYJ1LUEj2wog392g$HrqN4dK0uOpJ+WSTMtdRbB0k4IKShPtvPaMIy91lffc5DZnq4kwCYZCVGyX3HTCd+saPrVqFZGSc3MekVDX1Bg"))
print(verifyPassword("test1","$argon2id$v=19$m=32768,t=32,p=4$Do/qGLU0qCEf9Z2m395+SdjIlqlsYJ1LUEj2wog392g$HrqN4dK0uOpJ+WSTMtdRbB0k4IKShPtvPaMIy91lffc5DZnq4kwCYZCVGyX3HTCd+saPrVqFZGSc3MekVDX1Bg"))

# userAdd("user3","password")
userLogin("user3","password")
userLogin("user3","passwordd")
print(getUserId("user2"))