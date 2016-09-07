import MySQLdb

try:
	conn = MySQLdb.connect(host='localhost', user='root', passwd='openos', db='tornado', port=3306)
	cursor = conn.cursor()
	sql = "select * from user where name='%s' and id=%d"
	cursor.execute(sql % ('frank',1))
	print 'No sql injection ..'
	result = cursor.fetchall()
	for i in result:
		print i

	print 'After sql injection ...'
	cursor.execute(sql % ("foo' or 1=1;'--'",99))
#sql = "select * from user where name='foo' or 1=1--'' and id=1"
#	cursor.execute(sql)
	result = cursor.fetchall()
	for i in result:
		print i

	print cursor._executed
	cursor.close()
	conn.close()

except MySQLdb.Error, e:
	print "MySQL Error, %d,%s" %(e.args[0], e.args[1])

