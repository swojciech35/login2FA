from databaseconnect import queryDatabase

from databaseconnect import insertUser
from security import hashPassword
print(queryDatabase("select true"))

print(hashPassword("test"))
