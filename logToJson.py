# Dev: Rolando Vinicio Casigna Parra
# Date:18 sep 2016 09:03
#
# El siguiente script lee el archivo de logs para transformalos en JSON
#

import json
import string
import datetime
import couchdb

# Lectura del archivo
# El archivo debe estar al mismo nivel que el script
archivo = open("GPSTracker.log", "r")

# crea la conexion a la base de datos
db = server("http://192.168.1.8:5984/")

# Dando formato a la fecha
def formatoFecha(fecha):
	date_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

# 
# Es necesario trabajar esta cadena.
# Sat Sep 10 2016 18:31:38 GMT-0500 (ECT): 
# : onsrvUpdatePos: 359710044004092 - 359710044004092 
def primeraParte(partes):
	# separamos por los espacios
	p = partes[0].split(' ')

	# trabjando con la fecha 
	p1 = {"fecha":convertirFechaServidor(p),"dispositivo":obtenerDispositivo(p),"avl_data":obtenerDatosAVl(partes)}
	print p1

	# retorno el objeto contruido
	return p1
	
# Permite dar formato a la fecha del servidor
def convertirFechaServidor(f):
	#
	fechaPicada =  f[2] +"-"+ f[1]+"-"+ f[3] +" "+f[4]
	datetime.datetime.strptime(fechaPicada, "%d-%b-%Y %H:%M:%S")
	# imprimo la fecha del objeto
	return fechaPicada

def obtenerDispositivo(cad):
	avl = ''
	if (len(cad)>8):
		avl = cad[9]
	return avl

def obtenerDatosAVl (cad):
	avlData={}
	if (len(cad)>8):
		avlData={"fecha_avl":cad[1],"evento":cad[2],"latitud":cad[5],"longitud":cad[6],"evento1":cad[7],"evento1":cad[8],"evento1":cad[9]}
	return avlData

# Trabajo con toda la linea
#Fri Sep 09 2016 15:45:01 GMT-0500 (ECT): INFO: onsrvUpdatePos: 359710044007863 - 359710044007863 | 2016-09-09 15:45:00 | 30 | 0.00 | 6 | 0.922810 | -79.671558 | 0 | 0 | 0 | 0
def convertirLineaToJson(linea):
	#separamos la linea con los pipelnines 
	partes = linea.split('|')

	# llama a trabajar la primera parte de la linea.
	primeraParte(partes)

	# 
	convertirFechaServidor

#Envia a guardar la cadena
def persitirBase(jsonAVL):
	db = conectarBase(jsonAVL)
	

# Crea o se conecta a la la base de datos.
def conectarBase(jsonAVL):
	try:
    #Si no existe la Base de datos la crea
    pass
    db = server.create('quito')
except:
    #Caso contrario solo conectarse a la base existente
    db = server['quito']


def existeBase(idAvl):


# llamada principal
for linea in archivo.readlines():
	convertirLineaToJson(linea)
