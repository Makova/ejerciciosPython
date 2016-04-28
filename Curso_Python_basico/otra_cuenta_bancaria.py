#!/usr/bin/python
# -*- coding: utf-8 -*-

#  otra-cuenta_bancaria.py

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



"""
Excepciones propias de la clase CuentaBancaria
"""
class IngresoIncorrecto(Exception):
    pass

class RetiradaNegativa(Exception):
    pass

class RetiradaIncorrecta(Exception):
    pass

class RetiradaSuperiorSaldo(Exception):
    pass

class ErrorEnMovimientos(Exception):
    pass

class CuentaBancaria:
    def __init__(self, titular, ncuenta):
        self._titular = titular
        self._numero_de_cuenta = ncuenta
        self._saldo = 0
        self._movimientos = []
        
    def ingreso(self, cantidad):
        if cantidad >= 0:
            self._saldo += cantidad
            self._movimientos.append(['+',cantidad])
        else:
            raise IngresoIncorrecto()
        
    def retirar(self, cantidad):
        """ No se puede retirar efectivo si la cuenta no dispone de saldo   """
        try:
            if cantidad < 0:
                raise RetiradaNegativa()
        except:
            raise RetiradaIncorrecta()
        if (self._saldo - cantidad) < 0:
            raise RetiradaSuperiorSaldo()
        self._saldo -= cantidad
        self._movimientos.append(['-',cantidad])
    
    def saldo(self):
        return self._saldo
    
    def movimientos(self):
        for i in self._movimientos:
            if i[0] == "-":
                print "Retirada de: ", i[1], "€"
            elif i[0] == "+":
                print "Ingreso de:  ", i[1], "€"
            else:
                raise ErrorEnMovimientos()
        print "Saldo final: ", self._saldo, "€"


""" Pruebas """
""" ELIMINAR LINEA SI QUIERE PROBAR EL MENÚ DE PRUEBAS 
cuenta = CuentaBancaria("Fulano", 1234)
print "Menú de pruebas"
while True:
    try:
        print "\nElige la prueba a realizar:"
        print "1. Ingreso de 1000€"
        print "2. Ingreso de -20€"
        print "3. Retirada de 20€"
        print "4. Retirada de -20€"
        print "5. Retirada de 2000€"
        print "6. Consulta de saldo"
        print "7. Ver movimientos"
        print "0. Salir"
        
        opcion = int(input("Introduzca su elección: "))
        if opcion == 1:
            cuenta.ingreso(1000)
        elif opcion == 2:
            cuenta.ingreso(-20)
        elif opcion == 3:
            cuenta.retirar(20)
        elif opcion == 4:
            cuenta.retirar(-20)
        elif opcion == 5:
            cuenta.retirar(2000)
        elif opcion == 6:
            print cuenta.saldo()
        elif opcion == 7:
            cuenta.movimientos()
        elif opcion == 0:
            break
        else:
            print "Opción incorrecta, vuelva a elegir."
    except:
        print "ERROR"
ELIMINAR LINEA SI QUIERE PROBAR EL MENÚ DE PRUEBAS """


""" Menú del usuario de la cuenta """
cuenta = CuentaBancaria("Fulano", 1234)
print "\nEste programa realiza operaciones sobre su cuenta bancaria"
while True:
    try:
        print "\nLas operaciones que puede realizar son:"
        print "1. Ingresar"
        print "2. Retirar efectivo"
        print "3. Ver saldo"
        print "4. Ver movimientos"
        print "0. Salir"        
        opcion = int(input("Introduzca su elección: "))
        if opcion == 1:
            cuenta.ingreso(float(input("Introduzca la cantidad a ingresar: ")))
        elif opcion == 2:
            cuenta.retirar(float(input("Introduzca la cantidad a retirar: ")))
        elif opcion == 3:
            print "Su saldo actual es de: ", cuenta.saldo(), "€"
        elif opcion == 4:
            cuenta.movimientos()
        elif opcion == 0:
            break;                        
        else:
            print "Opción incorrecta, vuelva a elegir."
    except (IngresoIncorrecto) as e:
        print "Error al ingresar efectivo"
    except (RetiradaNegativa, RetiradaIncorrecta, RetiradaSuperiorSaldo):
        print "Error al retirar efectivo"
    except:
        print "Error vuelva a introducir los números"
print "Estamos a su disposición cuando quiera"
