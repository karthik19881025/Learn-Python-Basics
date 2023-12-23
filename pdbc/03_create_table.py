import pymysql


def create_table():
	con = pymysql.connect(host="localhost", user='root', password='root', database='college')
	cur = con.cursor()
	cur.execute("create table students (Name varchar(255), Marks int, position int)")
	print("Table created successfully")
	cur.close()
	con.close()


def insert_records():
	con = pymysql.connect(host="localhost", user='root', password='root', database='college')
	cur = con.cursor()
	cur.execute("insert into students values ('Ajay', 90, 5)")
	cur.execute("insert into students values ('Raju', 95, 3)")
	cur.execute("insert into students values ('Sneha', 97, 2)")
	cur.execute("insert into students values ('Karthik', 97, 2), ('Divya', 90, 5), ('Tanvika', 100, 1)")
	con.commit()
	print("Records inserted successfully")
	cur.close()
	con.close()


def retrieve_records():
	con = pymysql.connect(host="localhost", user='root', password='root', database='college')
	cur = con.cursor()
	cur.execute("select * from students")
	# output will be stored inside the cur1 object and need to access through for loop
	for row in cur:
		print(row)
	
	print("Records retrieved successfully")
	cur.close()
	con.close()


# create_table()
# insert_records()
retrieve_records()
