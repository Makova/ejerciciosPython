#!/usr/bin/python 
#coding: utf-8 

#  cuentaBancaria.py
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



class cuentaBancaria : 
	
	def __init__(self, titular, nCuenta, saldo, dineroIng, dineroRet) :
		self.titular = titular
		self.nCuenta = nCuenta
		self.saldo = saldo
		self.dineroIng = dineroIng
		self.dineroRet = dineroRet
		
	def IngresoDineroCuenta(self) : 
		self.dineroIng = input("Introduzca la cantidad de dinero a ingresar : ")
		self.saldo = self.saldo + self.dineroIng
		print "Saldo despues de haber ingresado : "
		return self.saldo
		
	def retirarDineroCuenta(self) : 
		if(self.saldo != 0) : 
			self.dineroRet = input("Introduzca la cantidad de dinero a retirar : ")
			self.saldo = self.saldo - self.dineroRet
			print "Saldo despues de haber sacado : "
			return self.saldo
		else : 
			print("Cuenta con saldo 0")
			return 0
			
	def getInfoCuenta(self) : 
		return self.titular, self.nCuenta, self.saldo, self.dineroIng, self.dineroRet

print ("=======================")
print (" BIENVENIDO A SU BANCO ")
print ("=======================")

print ("Lista de operaciones a realizar en la cuenta : ")
print ("1. Realizar un ingreso")
print ("2. Retirar dinero de su cuenta")
print ("3. Consultar saldo y movimientos de su cuenta")
print ("0. Terminar el programa")

opc = input("Introduzca un numero : ") 


while ((opc != 0) or (opc == 1) or (opc ==2) or (opc ==3)) :
	
	titular = raw_input("Introduzca quien es el titular de la cuenta : ")
	nCuenta = input("Introduzca el numero de cuenta : ")
	saldo = 0
	dineroIng = 0
	dineroRet = 0
	datos = cuentaBancaria(titular, nCuenta, saldo, dineroIng, dineroRet)
	
	if opc == 1 : 
		print datos.IngresoDineroCuenta() 
	elif opc == 2 : 
		print datos.retirarDineroCuenta()
	else : 
		print datos.getInfoCuenta()
			
	opc = input("Vuelva a introducir un numero de operacion : " )



