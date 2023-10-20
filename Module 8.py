from geopy.distance import great_circle
import mysql.connector
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='game',
         user='root',
         password='red.flower',
         autocommit=True
         )

#1.
mycursor = connection.cursor()
mycursor.execute("SELECT name, municipality, ident FROM airport")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

#2.
mycursor = connection.cursor()
country_code = input("Enter the country code (for example FI for Finland): ").upper()
mycursor.execute("SELECT name, type from airport WHERE iso_country = %s ORDER BY type", (country_code,))
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

#3.
mycursor = connection.cursor()
airport1 = input("Enter the ICAO if the first airport:").upper()
airport2 = input("Enter the ICAO if the second airport:").upper()
mycursor.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s OR ident = %s", (airport1, airport2))
results = mycursor.fetchall()


if len(results) < 2:
    print("ICAO code is not found in the database.")
else:
    coordi1 = (results[0][0], results[0][1])
    coordi2 = (results[1][0], results[1][1])

    distance = great_circle(coordi1, coordi2).kilometers

    print(f"Distance between {airport1} and {airport2}: {distance:.2f} kilometers")
