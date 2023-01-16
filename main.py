# Import bibliotek
import psycopg2 as db

# Połączenie z bazą danych PosgtreSQL
con = db.connect(host = "195.150.230.208", port = 5432, database = "2022_nazwisko_imie", user = "2022_nazwisko_imie", password = "*****")

# Utworzenie kursora
cursor = con.cursor()
# Tworzenie i wykonanie zapytania
cursor.execute("select true")
# Odczytanie wyników zapytania do kolekcji w formie listy
resultset = cursor.fetchall()

print(resultset[0][0])

# Zamknięcie połączenia
con.close()

