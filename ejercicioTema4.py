#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ejercicioTema4.py
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


def funcion(p1, p2, *p3):
    
lista[]
if p1 > 0:
    if p1 < p2:
        for i in range(p1, p2+1):
            lista.append(i)
    else:
        raise ValueError("La segunda debe ser mayor que la primera")
    else:
        raise ValueError("La primera debe ser mayor que 0")
    for i in p3:
        if lista.count(i) > 0:
            lista.pop(lista.index(i))
            
        return lista 
        
        
        #test 'funcion'
    print funcion(2, 16, 5, 7, 15, 13, 56)
        #print funcion(1, 2, 5, 7, 15, 13, 56)
