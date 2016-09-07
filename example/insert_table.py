import MySQLdb

try:
	conn = MySQLdb.connect(host='localhost', user='root', passwd='openos', db='tornado', port=3306)
	cursor = conn.cursor()
	for i in xrange(10):
		new_name= 'test_{0}'.format(i)
		new_id = '{0}'.format(i)
		cursor.execute("insert into user(name,id,age)VALUES(%s,%s,23)",(new_name,new_id,))
	conn.commit()
	cursor.close()
	conn.close()

except MySQLdb.Error, e:
	print "MySQL Error, %d,%s" %(e.args[0], e.args[1])

