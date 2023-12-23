import pymysql


class TargetAccountNotExists(Exception):
	pass


class SourceAccountNotExists(Exception):
	pass


class InsufficientFunds(Exception):
	pass


try:
	con = pymysql.connect(host="localhost", user='root', password='root', database='college')
	cur = con.cursor()
	saccno = input("Enter source account no: ")
	tamt = input("Enter transfer amount: ")
	
	q = 'select bal from customer where accno = ' + saccno
	q1 = 'update customer set bal = bal - ' + tamt + ' where accno = ' + saccno
	print(q1)
	
	cur.execute(q)
	p = tuple(cur)
	print(p)
	bal = p[0][0]
	print(bal)
	
	if bal > int(tamt):
		daccno = input("Enter destination account no: ")
		q2 = 'update customer set bal = bal + ' + tamt + ' where accno = ' + daccno
		print(q2)
		cur.execute(q1)
		if cur.rowcount == 0:
			raise SourceAccountNotExists
		
		cur.execute(q2)
		if cur.rowcount == 0:
			raise TargetAccountNotExists
		
		cur.close()
		con.commit()
		print(f'Transaction is successfully happened')
	else:
		raise InsufficientFunds

except InsufficientFunds:
	con.rollback()
	print(f'InsufficientFunds: {saccno} -> Source Account does not have enough funds to transfer the requested amount')
except SourceAccountNotExists:
	con.rollback()
	print(f'SourceAccountNotExists: {saccno} -> Transaction rollback happened')
except TargetAccountNotExists:
	con.rollback()
	print(f'TargetAccountNotExists: {daccno} -> Transaction Transaction rollback happened')
finally:
	if cur is not None:
		cur.close()
	if con is not None:
		con.close()
	print('Cursor & Connection got closed in finally block')
