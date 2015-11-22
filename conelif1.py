#!/usr/bin/env python
# -*- coding: utf-8 -*-

edad = int(input("¿Cuántos años tienes?"))
if edad >= 18:
	print ("Eres mayor de edad")
elif edad <= 17:
	print("Eres menor de edad")
elif edad <= 0:
	print("No se puede tener una edad negativa")
else:
	print"¿Seguro que tienes", edad, "años?"
