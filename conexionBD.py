import mysql.connector

dato = {
	'user' : 'root',
	'password' : '',
	'database' : 'tutorial',
	'host' : '127.0.0.1'
}

conexion = mysql.connector.connect(** dato)

cursor = conexion.cursor()
valores = "INSERT INTO usuarios(Id) VALUES ('123456')"
try:
	cursor.execute(valores)
	conexion.commit()
	print "se han insertado los valores en la base de datos"

except:
	print "no se han podido insertar valores en la base de datos"

conexion.close()