mycursor = mydb.cursor()
mycursor.execute("select * from user")

result = mycursor.fetchall()
for row in result:
    print(row)

mydb.commit()
mycursor.close()
mydb.close()
print(mycursor.rowcount,"record inserted.")    