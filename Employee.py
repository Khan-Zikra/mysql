# insert data in the table.
import mysql.connector as z
con= z.connect(host='localhost',
               user='root',
               password='bhoolgayi',
               database='zikra2')

cursor=con.cursor()
while True:
    code=int(input("Enter code :"))
    name=input("Enter Name :")
    salary=int(input("Enter salary :"))
    query="Insert into emp values ({} ,'{}',{})".format(code, name, salary)
    cursor.execute(query)
    con.commit()
    print("Data inserted successfully..")
    a=int(input("1->Enter More \n2->Exit\nEnter choice :"))
    if a==2:
        break
