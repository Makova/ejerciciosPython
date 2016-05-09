#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  metodos.py
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


cad = "Hola Mundo !"

print cad[2]
print cad[2:5]
print cad[6:]
print cad[:9]

print len(cad)
print cad.count("o")
print cad.endswith("!")
print cad.find("M")
print cad.rfind("o")
print cad.upper()
print cad.replace("","_")

tupla = ["Carlos","Lopez", "Diaz"]
c= ","
print c.join(tupla)
