import MySQLdb


try:
	conn = MySQLdb.connect(host='localhost', user='root', passwd='openos', db='tornado', port=3306)
	cursor = conn.cursor()
	cursor.execute('create table user ( name varchar(32), id int, age int)')
	cursor.close()
	conn.close()
except MySQLdb.Error, e:
	print "MySQL Error %d: %s" % (e.args[0], e.args[1])
