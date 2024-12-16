import pymysql

# Define MySQL credentials
username = "root"          # Replace with your MySQL username
password = "123456" 
host = "localhost"     # Replace with your MySQL password
database = "Student_Management_System"

# Establish a database connection
conn = pymysql.connect(
    host=host,
    user=username,
    password=password,
    database=database
)

cursor = conn.cursor()
