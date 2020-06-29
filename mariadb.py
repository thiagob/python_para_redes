# Pré-requisito pip install mysql-connector-python
import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.1.100",
  user="root",
  password="root",
  database="MyVideos116"
)

# https://kodi.wiki/view/Databases
query = "SELECT c00, c16, c14 FROM movie ORDER BY c00 LIMIT 100"

cursor = mydb.cursor()
cursor.execute(query)
for (c00, c16, c14) in cursor:
    print(c00)
