import mysql.connector
import os,sys
def Menu():
	print ""
	print "################################################"
	print "################ Menu Principal ################"
	print "################################################"
	print ""
	print "1. Agregar articulos"
	print "2. Modificar articulos"
	print "3. Eliminar articulos"
	print "4. Ver Articulos"
	print "5. Salir"
	try:
		OP=int(input("Introduzca la accion que desea: "))
	except:
		print "Esto no es un numero"
		print ""
		Menu()
	os.system('cls')
	Seleccion(OP)

def Seleccion(var):
	if var==1:
		Agregar()
	if var==2:
		Modificar()
	if var ==3:
		Eliminar()
	if var==4:
		Listar()
	if var==5:
		Salir()
	else:
		print "Listar un numero de la lista"

def Agregar():
	print "**********************"
	print "** MENU AGREGAR ******"
	print "**********************"
	print ""
	print "A continuacion digite los datos"

	Nombre = raw_input("Digite el nombre del articulo: ")
	Precio = input ("Digite el precio del articulo: ")
	#conexion()
	data ={
	'user' : 'root',
	'password' : '',
	'database' : 'articulos',
	'host' : '127.0.0.1'
	}
	conn = mysql.connector.connect(** data)
	cursor = conn.cursor()
	valores = "INSERT INTO productos(Nombre, Precio) VALUES ('"+Nombre+"', '%i')" % Precio
	try:
		cursor.execute(valores)
		conn.commit()
		print "se ha insertado correctamente los valores"
	except:
		print "no se logro insertar"
	conn.close()
	#cerrar_conexion(conn)
	Menu()

def Modificar():
	producto=[]
	data ={
	'user' : 'root',
	'password' : '',
	'database' : 'articulos',
	'host' : '127.0.0.1'
	}
	conn = mysql.connector.connect(** data)
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM  productos")
	print "**********************"
	print "** MENU MODIFICAR ****"
	print "**********************"
	print ""

	for productos in cursor:
		producto.append (productos)
		product = '\t'+str(productos[0])+ '\t' +str(productos[1])+ '\t' +str(productos[2])
		print (str(product))
		print ""
	cod = input ("Digite el codigo del producto a modificar")
	
	for productos in producto:
		if int(productos[0]) == int(cod):
			nombre = productos[1]
			precio = productos[2]
			encontrado = True
			break
	nombre = raw_input("Digite el nombre nuevo"+ nombre +":")
	precio = input("Digite el precio nuevo"+str(precio)+":")
	sql = "UPDATE productos SET Nombre='%s'"%nombre +",Precio='%i'" %precio + " WHERE Id='%i' " %cod
	cursor.execute(sql) 
	conn.commit()
	conn.close()
	os.system('cls')
	print "El producto se ha modificado"
	print sql
	Menu()

def Eliminar():
	data ={
	'user' : 'root',
	'password' : '',
	'database' : 'articulos',
	'host' : '127.0.0.1'
	}
	conn = mysql.connector.connect(** data)
	cursor = conn.cursor()
	cursor = conn.cursor()
	comando = "SELECT * FROM productos" 
	cursor.execute(comando)
	print "**********************************"
	print "********* OPCION ELIMINAR ********"
	print "**********************************"
	print ""
	print ""
	print "\t Id \t Nombre \t Precio"
	#print "**************************"
	for productos in cursor:
		product = '\t'+str(productos[0])+ '\t' +str(productos[1])+ '\t' +str(productos[2])
		print product
	print ''
	cod= input("Digite el codigo del producto")
	sql= "DELETE FROM productos WHERE Id='%i'" %cod
	cursor.execute(sql)
	conn.commit()
	conn.close()
	Menu()

def Listar():
	print "**********************************"
	print "***** SE LISTARAN LOS DATOS ******"
	print "**********************************"
	print ""

	data ={
	'user' : 'root',
	'password' : '',
	'database' : 'articulos',
	'host' : '127.0.0.1'
	}
	conn = mysql.connector.connect(** data)
	cursor = conn.cursor()
	comando = "SELECT * FROM productos" 
	cursor.execute(comando)
	try:
		print ""
		print "\t Id \t Nombre \t Precio"
		#print "**************************"
		for productos in cursor:
			product = '\t'+str(productos[0])+ '\t' +str(productos[1])+ '\t' +str(productos[2])
			print product
		conn.commit()
	except:
		print "no se logro listar"
	conn.close()
	print ''
	Menu()


def Salir():
	print"Has elegido la opcion salir"
	sys.exit()

Menu()