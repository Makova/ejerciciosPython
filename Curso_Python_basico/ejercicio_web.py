#!/usr/bin/python
# _*_  coding: utf-8  _*_

#  ejercicio_web.py
 	
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


import urllib2
import sys
import string
from urllib2 import Request, urlopen, URLError, HTTPError

url = raw_input('¿De qué página quieres obtener el código html?: (Indicar dirección url completa) ')
nombre_archivo = raw_input('¿Con qué nombre quieres almacenar el archivo?: ')


def almacenar_codigo(url) : 
  
    try:
        # Creamos un objeto request con la URL que queremos y con la cabecera copiada de un navegador
        req = urllib2.Request(url, headers= {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"})
        # Usamos la request para hacer la petición
        html = urllib2.urlopen(req)
        headers = html.info() # Leer las cabeceras
        data = html.read() # Leer los datos
        salida = open('código_HTML_%s.txt'%(nombre_archivo),'w') # Abrimos fichero de texto
        salida.write('Url: ' + html.geturl() + '\n' + 'Hora/Fecha: ' + headers['date'] + '\n' + 'Longitud del código: ' +  str(len(data)) + '\n' + '\n' + 'Datos html: ' + '\n' + data)
        salida.close() # cerramos fichero de texto
        html.close()
 
    # Excepción para el caso de que no se introduzca el código html
    except ValueError :
        url = 'http://' + url

    # Excepción para errores tipo http en el que se realiza conexión pero no existe el fichero pedido: error tipo 404.
    except HTTPError as error:
        print 'El servidor no puede cumplir con la solicitud.'
        print 'Código de error: ', error.code
   
    # Excepción para errores URL, es decir, no se puede realizar la conexión con servidor 
    except URLError as error:
        print 'No se ha encontrado la página indicada'
        print  'Razón:', error.reason  

almacenar_codigo(url)       


    
