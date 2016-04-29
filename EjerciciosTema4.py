#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ejerciciosTema4.py
#  
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
#  
#  


#!/usr/bin/python
#coding: utf-8

# Nota que, en el valor que recibe la función, tiene 'cancion="lalala"'
# Canción es la variable, como siempre, y "lalala" es lo que se le asignará por defecto si no se le pasa ningún valor
def canta(cancion="lalala"):

    if cancion == "lalala":
        print "Laaa, lala laaa,  lala laaa,  lala laaaaaaa..."
    elif cancion == "himno":
        print "Naaana, naaana, nanana nana nana na na NA na NA..."
    elif cancion == "daisy":
        print "Lo siento Dave, me temo que no puedo hacer eso."
    else:
        print "Esa no me la sé"

#Asignándole un valor hace lo previsible.
print "Pasando \"daisy\" nos responde:"
canta("daisy")

# pero, si no le asignamos ningún valor, toma el que tiene por defecto en la función
print "Pero, si no pasamos nada, dice:"
canta()
