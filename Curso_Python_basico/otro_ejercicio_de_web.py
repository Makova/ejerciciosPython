#!/usr/bin/python
# -*- coding: utf-8 -*-

#  otro_ejercicio_de_web.py

#  Copyright 2016 Manu <makova65@gmail.com>
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
while condition is False : 
	print ('El fichero no existe o no se encuentra en este directorio')
	break
else :  
	csvfile = open(str(csv), "rb")
	 
htmlfile = open( str(raw_input('Introduzca el nombre del archivo a obtener (sin extension)')+'.html') , "w")

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

  
