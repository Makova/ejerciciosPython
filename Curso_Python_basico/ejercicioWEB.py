#!/usr/bin/python
# -*- coding: utf-8 -*-

#  ejercicioWEB.py
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

import csv
import os

#leer archivo csv
csv = raw_input('Introduzca el nombre del archivo que contiene la informacion (sin  extension)')+'.csv'
dirname = os.getcwd() #proporciona el nombre del directorio
files = os.listdir(dirname) #crea una lista con los archivos que hay en ese directorio

if csv not in  files: 
	condition = False

# PROFESOR: En el bloque de arriba haces condition = False si no existe el archivo. Vale.
# PROFESOR: pero ¿Y si el archivo sí que existe? entonces condition no está definida y,
# PROFESOR: al tratar de usarla en el bloque de abajo, dará siempre error

while condition is False : 
	print ('El fichero no existe o no se encuentra en este directorio')
	break
else :  
	csvfile = open(str(csv), "rb")
    # PROFESOR: raw_input ya retorna un string, no hace falta convertirlo de nuevo.

# PROFESOR: Por otr lado, este bloque while no tiene sentido:
# PROFESOR: al tener un break sin ninguna condición sólo se ejecuta una vez, por lo que es un bucle sin bucle.
# PROFESOR: pero la condición (condition) no cambia, por lo que si no tuvieras el break
# PROFESOR: nunca saldrías y entrarías en un bucle infinito.
#
# PROFESOR: Creo que lo que quieres hacer aquí lo puedes hacer de forma mucho más fácil con una estructura try.
# PROFESOR: Dale un vistazo aquí: http://campusvirtual.ugr.es/moodle/mod/resource/view.php?id=150201
 
htmlfile = open( str(raw_input('Introduzca el nombre del archivo a obtener (sin extension)')+'.html') , "w")
# PROFESOR: Como antes, raw_input ya retorna un string, no hace falta convertirlo de nuevo.

#escribir cabecera de la tabla
htmlfile.write( "<meta http-equiv= Content-type content=text/html;charset=UTF-8 />" )
htmlfile.write( "<table border=1>\n" )
htmlfile.write( "<tr>\n" )
htmlfile.write( "<td align=center valing=middle>Nombre</td>\n" )
htmlfile.write( "<td align=center valing=middle>Apellido1</td>\n" )
htmlfile.write( "<td align=center valing=middle>Apellido2</td>\n" )
htmlfile.write( "<td align=center valing=middle>Email</td>\n" )
htmlfile.write( "<tr>\n" )

#escribir el resto de filas   

fieldnames = ['Nombre', 'Apellido1', 'Apellido2', 'Email']
reader = csv.DictReader(csvfile,fieldnames=fieldnames)

# PROFESOR: csv es el nombre del módulo,
# PROFESOR: pero también es la variable con el nombre del fichero cvs que pediste al usuario
# PROFESOR: has liado a Python, que cree que intentas acceder a un atributo de la cadena que no exsite
# PROFESOR: Por eso te da el error de "'str' object has no attribute 'DictReader'"
# PROFESOR: Lo más fácil es cambiar el nombre de la variable csv por otro que no dé conflicto

for row in reader: 
    htmlfile.write( "<tr>\n" )
	# Concatenar las cadenas "<td align=center valing=middle>" y "</td>\n"  con row['Nombre'] en medio, fuera de las comillas
	# para que tome el valor de row['Nombre'] 
	
    htmlfile.write( "<td align=center valing=middle>"+row['Nombre']+"</td>\n" )
    htmlfile.write( "<td align=center valing=middle>"+row['Apellido1']+"</td>\n" )
    htmlfile.write( "<td align=center valing=middle>"+row['Apellido2']+"</td>\n" )
    htmlfile.write( "<td align=center valing=middle>"+row['Email']+"</td>\n" )
    htmlfile.write( "<tr>\n" )

    #finalizar la tabla
htmlfile.write( "</table>\n" )
htmlfile.close()

  
