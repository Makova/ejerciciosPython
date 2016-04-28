#!/usr/bin/python
# -*- coding: utf-8 -*-

#  ejercicio_web1.py

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

# Escribe un script que obtenga el código html de una web y lo almacene en un fichero de texto.
# Toda mejora se tendrá en cuenta aparte de lo que se pide en el ejercicio.

# Usar clases
# Usar try-catch
# Usar if else
# usar for y while



# Módulos
import os
import urllib2

os.system ("clear")
class procesarURL():
	def __init__(self,url):
		self.url = url
	def mostrarURL(self, url):
		web = urllib2.urlopen(self.url)
		html = web.read()
		print html
	def guardarURL(self, url):
		web = urllib2.urlopen(self.url)
		html = web.read()
		f=open("web.txt","w")
		f.write(html)
		f.close()
		print "Código HTML guardado en web.txt"
	def checkURL(self, url):
		try:
			web = urllib2.urlopen("http://" + site)
		except urllib2.URLError:
			print "Error, no has escrito una URL correcta o no se puede obtener"
			quit()

site = raw_input("Que web quieres consultar?  ")

url = procesarURL("http://" + site)

url.checkURL(url)

opcion = raw_input("1.Mostrar código\n2.Guardar código en un fichero\nOpcion? ")

if int(opcion) == int(1) :
  	url.mostrarURL(url)
elif int(opcion) == int(2) :
   	url.guardarURL(url)
