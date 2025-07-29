//print the name
//print("thanu")
# -------------------------------------------------------------------
// print message
msg = input("enter message")
print(msg)
# ------------------------------------------------------------------------
Determination
age = int(input("Enter your age:"))
if age <=10:
    print("Child")
else:
    print("Not a child")
if age >=10:
    print("Adult")
else:
    print("Not a Adult")
# -------------------------------------------------------------------
display the number from 1 to 10
for i in range(1,10):
    print(i)
# ----------------------------------------------------------------
Starts from 0,1,2,3...
cars = ["Ford","Volvo","BMW","TATA"]
To find the length of the array
print(len(cars))
access the 8th position
print(cars[2])
for i in range(len(cars)):
    print(cars[1])

for i in cars:
        print(i)
# ------------------------------------------------------------
List = ["one","two","three"]
print(list[2])
except Exception as e;
 print("error")
 with open("sample,txt", 'w') as file:
      file,write("some text")
# --------------------------------------------------------------
check a number is even or odd
num = int (input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
    sum of two numbers
num1 = int(input("Enter the first  number: "))
num2 = int(input("Enter the second number: "))
sum = num1 + num2
print(f"The sum of {num1} and {num2} is {sum}")
if num.isnumeric() == False:
     raise("number1 is not number")
else if num2,isnumeric() == False:
     raise("number2 is not number")
else:
     res = int(num)+int(num2)
     print(str(res))
except Exception as e:
     print(e)          
     if number is greater than 100     
num = int(input("Enter a number: "))
# ------------------------------------------------------------
if num > 100:
    print("The number is greater than 100.")
else:
    print("The number is than 100.")
    Check the number is pos neg or zero 
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
convert int to float
int_num = 42
float_num = float(int_num)
print(f"Integer {int_num} converted to float: {float_num}")
# convert float to int
original_float = 7.9
converted_int = int(original_float)
print(f"Float {original_float} converted to integer: {converted_int}")
Prompt the user to enter three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
# -----------------------------------------------------------------------------
#01 Find the largest using if-elif-else
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (11num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print(f"The largest number is: {largest}")
operations
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Select operation: add for addition, sub for subtraction, mul for multiplication, div for division")
operator = input("Enter operation (+, -, *, /): ")
if operator == 'add':
    result = num1 add num2
    print(f"{num1} add {num2} = {result}")
elif operator == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operator == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator selected.")
# ---------------------------------------------------------------------------------------------------------
    to count the characters in string
text = "Thanushree"
character_count = len(text)
print("Total characters:", character_count)
# ---------------------------------------------------------------
# Counting how many letters are there in the string
text = "Thanu"
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
for char, count in char_count.items():
    print(f"'{char}' appears {count} time(s)")
-------------------------------------------------------------
    # define the method 
    def add():
        print("this ")
name = "awsedf"
age = 45
print(f"Name is {name} and his age is {age},")
text = f"Name is {name}, and his age is {age}"
print(text)
# --------------------------------------------------------------------------------------------------------------------------
#  get the input from the user and call the function
def print_user_info(name, city):
   text = f"Name is (name), and his city is (city)"
   print(text)
#    -------------------------------------------------------------------------------------------
# print date and time using python function
import datetime
def print_current_datetime():
now = datetime.datetime.now()
print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))
print_current_datetime()
# ------------------------------------------------------------------------------------------------
from datetime import datetime
def calculate_age():
    dob_str = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        birthdate = datetime.strptime(dob_str, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birthdate.year - (
            (today.month, today.day) < (birthdate.month, birthdate.day)
        )
        print("Your age is:", age)
    except ValueError:
        print("Invalid format. Please enter the date in YYYY-MM-DD format.")
calculate_age()
# --------------------------------------------------------------------------------------------------------
import mysql.connector

# print("Connected to the database successfully")
def insert_data(id,name,email,mobile):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="roottoor",
        database="thanu_ece"
)
    mycursor = mydb.cursor()
    sql = "INSERT INTO user (id,name,email)VALUES (%s,%s,%s,%s)"
    val = [id,name,email,mobile]
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.close()
    mydb.close()
    print(mycursor.rowcount, "record inserted.")

id = input("enter the id")
name = input("enter the name")
email = input("enter the email") 
mobile= input("enter the mobile") 
insert_data(id,name,email,mobile)