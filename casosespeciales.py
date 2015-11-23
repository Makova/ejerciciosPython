#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  casosespeciales.py
#  
#  Copyright 2015 Manu <makova65@gmail.com>
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

numero = input("Dígame un número: ")
if numero % 8 == 0:
    print(numero), "es múltiplo ocho, de cuatro y de dos"
elif numero % 4 == 0:
    print(numero), "es múltiplo de cuatro y de dos"
elif numero % 2 == 0:
    print(numero), "es múltiplo de dos"
else:
    print(numero), "no es múltiplo de dos" 
