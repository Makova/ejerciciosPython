#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ejercicioDatosBancarios.py
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

import datetime

class cuentaBancaria:
    titular = ""
    numero = 0
    saldo = 0
    movimientos = []

    def __init__(self,tit,num,sal):
        self.titular = tit 
        self.numero = num
        self.saldo = sal
        if sal < 0:
            self.saldo = 1000

    def ingresar(self,cantidad):
        if cantidad <= 0:
            print "----------------------------------------------"
            print "Es una cantidad erronea"
            print "----------------------------------------------"
        else:
            self.saldo += cantidad
            print "----------------------------------------------"
            print "INGRESO"
            print "Ha ingresado " + str(cantidad) + " euros"
            print "Su nuevo saldo es " + str(self.saldo) + " euros"
            print "----------------------------------------------"
            self.movimientos.append("Ingreso de " + str(cantidad) + " euros a fecha  " + str(datetime.datetime.utcnow()))
    def retirar(self,cantidad):
        if cantidad > self.saldo:
            print "No tiene suficiente saldo"
        else:
            self.saldo -= cantidad
            print "----------------------------------------------"
            print "RETIRADA"
            print "Ha retirado " + str(cantidad) + "euros con exito"
            print "Su nuevo saldo es " + str(self.saldo) + " euros"
            print "----------------------------------------------"
            self.movimientos.append("Retirada de " + str(cantidad) + " euros a fecha " + str(datetime.datetime.utcnow()))
    def saldoActual(self):
        print "----------------------------------------------"
        print "Saldo:" + str(self.saldo) + " euros"
        print "----------------------------------------------"
    def movs(self):
        print "----------------------------------------------"
        print "ULTIMOS MOVIMIENTOS y SALDO:"
        for m in self.movimientos:
            print m
        print "Saldo:" + str(self.saldo) + " euros"
        print "----------------------------------------------"
    def datosPersonales(self):
        print "----------------------------------------------"
        print "DATOS BANCARIOS"
        print "Titular:"
        print self.titular
        print "Num. Cuenta:"
        print self.numero
        print "----------------------------------------------"
cuenta = cuentaBancaria("Pepe","231231333",120)
cuenta.ingresar(10)
cuenta.retirar(20)
cuenta.saldoActual()
cuenta.movs()
cuenta.datosPersonales()
