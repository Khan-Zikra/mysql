import mysql.connector
conn = mysql.connector.connect(host= "localhost", password= "bhoolgayi",user= "root")
if conn.is_connected():
    print("Connection varify") 