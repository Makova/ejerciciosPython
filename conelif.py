#!/usr/bin/env python
# -*- coding: utf-8 -*-

edad = int(input("¿Cuántos años tiene? "))
if edad < 0:
    print("No se puede tener una edad negativa")
elif edad < 18:
    print("Es usted menor de edad")
elif edad <= 101:
    print("Es usted mayor de edad")
elif edad >=102:
    print("No puede ser")	
else:
    print("¿Seguro que tiene", edad, "años?")
