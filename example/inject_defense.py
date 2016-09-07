import MySQLdb

try:
	conn = MySQLdb.connect(host='localhost', user='root', passwd='openos', db='tornado', port=3306)
	cursor = conn.cursor()
	sql = "select * from user where name='%s'"
#	cursor.execute(sql % ("invalid username' or 1=1;--''")) # Bad 
	cursor.execute(sql, ("invalid username' or 1=1;--''",)) # Good
	result = cursor.fetchall()
	for i in result:
		print i

	cursor.close()
	conn.close()

except MySQLdb.Error, e:
	print "MySQL Error, %d: %s" % (e.args[0],e.args[1])
