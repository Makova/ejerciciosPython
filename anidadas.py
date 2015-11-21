#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("Piense un número de 1 a 4.")
print("Conteste S (sí) o N (no) a mis preguntas.")
primera = raw_input("¿El número pensado es mayor que 2? ")
if primera == "S":
    segunda = raw_input("¿El número pensado es mayor que 3? ")
    if segunda == "S":
        print("El número pensado es 4.")
    else:
        print("El número pensado es 3")
else:
    segunda = raw_input("¿El número pensado es mayor que 1? ")
    if segunda == "S":
        print("El número pensado es 2.")
    else:
        print("El número pensado es 1.")
print("¡Hasta la próxima!")
