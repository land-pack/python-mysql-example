import MySQLdb 

try:
	conn = MySQLdb.connect(host='localhost', user='root', passwd='openos', db='tornado', port=3306)
	cursor = conn.cursor()
	cursor.execute("select * from user")
	results = cursor.fetchall()
	for r in results:
		print r


	cursor.close()
	conn.close()


except MySQLdb.Error, e:
	print "MySQL Error : %d, %s" % (e.args[0], e.args[1])
