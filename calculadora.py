# X-Serv-13.5-Calculadora
#!/usr/bin/python

import sys

if len(sys.argv) != 4:
	print
	sys.exit ("Instrucciones: funcion operando1 operando2")

operacion = sys.argv [1]
if operacion not in ['+', '-', 'x', '/']:
	sys.exit ("Operaciones disponibles: +  -  x  /")

operando1 = float (sys.argv [2])
operando2 = float (sys.argv [3])

if operacion == '+':
	print operando1 + operando2
elif operacion == '-':
	print operando1 - operando2
elif operacion == 'x':
	print operando1 * operando2
elif operacion == '/':
	print operando1 / operando2
else:
	sys.exit ("Excepcion")