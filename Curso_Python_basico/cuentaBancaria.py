#!/usr/bin/python 
#coding: utf-8 

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



