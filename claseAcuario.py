#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  claseAcuario.py
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

# Ejemplo de clase.

class Acuario():

    #El método __init__ se ejecuta automáticamente al llamar a la clase
    def __init__(self, litros, tipo, num):
        self.capacidad = litros
        self.tipo = tipo
        self.total_peces = num

    def meter_pez(self):
        self.total_peces = self.total_peces + 1

    def sacar_pez(self):
        if ( self.total_peces > 0):
            self.total_peces = self.total_peces + 1

Mipecera= Acuario(100, "tropical", 5)

print "La pecera tiene", Mipecera.capacidad, "litros"
print "Hay", Mipecera.total_peces, "peces"

print "Añadimos un pez"

Mipecera.meter_pez()

print "Ahora hay", Mipecera.total_peces, "peces"
