#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  otraClase.py
#  
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


class Complejo:
    
    def __init__(self, parteReal, parteImaginaria):
        """Constructor de la clase Complejo"""
        self.r = parteReal
        self.i = parteImaginaria
        
    def getReal(self):
        return self.r
        
    def getImag(self):
        return self.i
        
num = Complejo(3.0,-4.5)
print "Parte Real ", num.getReal()
print "parte Imaginaria ", num.getImag()
