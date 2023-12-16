"""
Python Database Connection (PDBC)

Python to connect with any database, we require a module.
Python to connect with mysql, we require a module called pymysql.
Python to connect with oracle, we require a module called cx_oracle.
Python to connect with sqlserver, we require a module called pyodbc.
pymysql is an external module (which is not part of python in built core libraries).
pip is a component (package manager) we need to use it for downloading and installing of any external modules.
pip - preferred installer program

1. connection objects: If we call connect() function by providing the following connection parameters,
then a connection object is created.

a. hostname
b. username
c. password
d. database name

ex: con=pymysql.connect(host="localhost", user="root", password="root", database="employees")

here con is a connection object.  We can provide any name

2. cursor objects: on a connection object (con), if we pass cursor() method then a cursor object will be created.

ex: cur1 = con.cursor()

Through the cursor object(cur1), we can access "execute()" method.
As part of the "execute()" method, we can specify any valid sql query as arguments.

ex: cur1.execute("select * from employees")

"""