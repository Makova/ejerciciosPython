#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  verdadero_falso.py
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


resultado = 3 == 2

print resultado
# 3 no es igual a 2, por lo que es falso

print True and True
# algo que es "cierto y cierto" es cierto

print True and resultado
# algo que es "cierto y falso" es falso

print not True
# "no cierto" es falso

print False or resultado
# algo que es "falso o falso" es falso
