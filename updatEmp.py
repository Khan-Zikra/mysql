import mysql.connector as a
con=a.connect(host="localhost",
              user="root",
              password="bhoolgayi",
              database="zikra2")

cursor=con.cursor()
code=int(input("Enter your code :"))
salary=int(input("Enter your salary :"))
#query="update emp set salary=70000 where code=103"
query="update emp set salary={} where code={}".format(salary,code)
cursor.execute(query)
con.commit()
if cursor.rowcount>0:
   print("Data Updated Successfully...")
else:
    print("No data found.")
