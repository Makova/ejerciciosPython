#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  clases.py
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


class Cesta:

# Recuerde siempre el argumento self
    def __init_(self,contenido=None):
        self.contenido = contenido or []
    
    def anadir(self,elemento): 
        elf.contenido.append(elemento)
    
    def muestra_me(self):
        resultado = ""
        for elemento in self.contenido:
            resultado = resultado + " " + `elemento`
        print "Contiene:"+resultado
