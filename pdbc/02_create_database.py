# steps to create a new database within mysql via python code

import pymysql


def create_database():
	con = pymysql.connect(host="localhost", user="root", password="root")
	cur = con.cursor()
	cur.execute("create database college")
	print("Database Created Successfully")
	cur.close()
	con.close()


def drop_database():
	con = pymysql.connect(host="localhost", user="root", password="root")
	cur = con.cursor()
	cur.execute("drop database college")
	print("Database Dropped Successfully")
	cur.close()
	con.close()


create_database()
# drop_database()
