import os
from mysql.connector import connect, Error

# Replace with your connection details
mydb = connect(
    host="localhost",
    user="root",
    password="14523512Newel",
    database="university_system"
)

mycursor = mydb.cursor()
# Execute SQL statements using the execute() method on the cursor

# Close connection to the databasse  
mycursor.close()
mydb.close()