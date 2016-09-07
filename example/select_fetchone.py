import MySQLdb

try:
	conn = MySQLdb.connect(host='localhost', user='root', passwd='openos', db='tornado', port=3306)
	cursor = conn.cursor()
	count = cursor.execute('select * from user')
	print 'count:',count
	result = cursor.fetchone()
	print 'one recored:',result
	cursor.close()
	conn.close()
except MySQLdb.Error, e:
	print "MySQL Error %d: %s" % (e.args[0], e.args[1])

	
