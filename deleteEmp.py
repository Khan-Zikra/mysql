import mysql.connector as b
con=b.connect(host="localhost",
              user="root",
              password="bhoolgayi",
              database="zikra2")

cursor=con.cursor()
code=int(input("Enter Employee code to Delete:"))
#a="delete from emp where code=104"
a="delete from emp where code={}".format(code)
cursor.execute(a)
con.commit()
if cursor.rowcount>0:
   print("Deletion Successfully...")
else:
    print("Employee code not Found")