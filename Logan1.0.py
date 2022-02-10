#!/usr/bin/python3
print("BY: GABRIEL LOGAN")
print()
print("Many Calculator = Logan1.0")
print()

import math

def Adção():
    a = float(input("Digite um numero para somar: "))
    b = float(input("Digite outro para completar a soma: "))
    resu = a+b
    print()
    print(a, "+", b, " = %.2f" %resu)
    print()
    print("Obrigado por usar minha Calculadora by = Gabriel Logan")

def Subtração():
    a = float(input("Digite um numero para subtrair: "))
    b = float(input("Digite outro para completar a subtração: "))
    resu = a-b
    print()
    print(a, "-", b, " = %.2f" % resu)
    print()
    print("Obrigado por usar minha Calculadora by = Gabriel Logan")

def Multiplicação():
    a = float(input("Digite um numero para Multiplicar: "))
    b = float(input("Digite outro para completar a Multiplicação: "))
    resu = a * b
    print()
    print(a, "x", b, " = %.2f" % resu)
    print()
    print("Obrigado por usar minha Calculadora by = Gabriel Logan")

def Divisão():
	a = float(input("Digite um numero para dividir: "))
	b = float(input("Digite outro para dividir :"))
	divsor = a/b
	divsosobra = a%b
	print()
	print(a, "/", b, "= %.2f" %divsor)
	print()
	print("A sobra da divisão =%.2f"%divsosobra)
	print()
	print("Obrigado por usar minha Calculadora by = Gabriel Logan")

def Calcular_apenas_delta():
	print()
	numA = float(input("Digite o valor de A: "))
	numB = float(input("Digite o valor de B: "))
	numC = float(input("Digite o valor de C: "))
	rdelta = numB**2-4*numA*numC
	print()
	print(numB,"Ao quadrado -4 vezes", numA, "vezes", numC, "= %2.f" %rdelta)
	print()
	print("Delta = %.2f" %rdelta)
	print()
	print("Obrigado por usar minha Calculadora by = Gabriel Logan")

def Formula_de_Bhaskara():
	print()
	numA = float(input("Digite o valor de A: "))
	numB = float(input("Digite o valor de B: "))
	numC = float(input("Digite o valor de C: "))
	rdelta = numB**2-4*numA*numC
	print()
	print(numB,"Ao quadrado -4 vezes", numA, "vezes", numC, "=", rdelta)
	print("Delta = ", rdelta)
	print()
	print("Agora - Calcular a Raiz Quadrada: !!!")

	varhaha1 = math.sqrt(float(input("Digite o valor de DELTA: ")))

	print("A Raiz de Delta = %.2f" %varhaha1)
	print("Formula de BHASKARA Calculadora")
	print()
	numD = float(input("Digite o valor da raiz de DELTA: "))
	numB = float(input("Digite o valor de B: "))

	baskara = -numB+numD
	baskaran = -numB-numD

	print(-numB, "+", numD, "=", baskara)
	print(-numB, "-", numD, "=", baskaran)

	numA = float(input("Digite o valor de A : "))

	bascaraa = baskara/(numA*2)
	bascaraa2 = baskaran/(numA*2)

	print(baskara, "Dividido por", numA, "Vezes 2 = %.2f" %bascaraa2)
	print(baskaran, "Dividido por", numA, "Vezes 2 = %.2f" %bascaraa)
	print()
	print("X1 = %.2f" %bascaraa2)
	print("X2 = %.2f" %bascaraa)
	print()
	print("Obrigado por usar minha Calculadora by = Gabriel Logan")

def Conometro():
	import time
	print("Bem vindo ao Rolão do Tempo; CONOMETRO")
	print()
	print("Digite um numero inteiro, caso contrario falhara.")
	print("OBS: A contagem é em segundos!")

	zero = 0 
	limi = 999999999999999999
	x = int(input("Digite o seu tempo: "))

	while zero < limi:
		zero += 1
		time.sleep(0.9)
		print(zero)
		if zero == x:
			break

	print()
	print("Obrigado por usar nosso Conometro; by: Gabriel Logan")

print("QUAL OPERACAO MATEMATICA ESCOLHE ?")
print("1.Adção")
print("2.Subtração")
print("3.Multiplicação")
print("4.Divisão")
print("5.Calcular_apenas_delta")
print("6.Formula_de_Bhaskara")
print("7.Conometro")

escolha = input("Digite a operação desejada(1/2/3/4/5/6/7): ")

if escolha == '1':
	Adção()
else:
	if escolha == '2':
		Subtração()
	else:
		if escolha == '3':
			Multiplicação()
		else:
			if escolha == '4':
				Divisão()
			else:
				if escolha == '5':
					Calcular_apenas_delta()
				else:
					if escolha == '6':
						Formula_de_Bhaskara()
					else:
						if escolha == '7':
							Conometro()
						else:
							print("ERRO, Digite apenas 1, 2, 3, 4, 5, 6, qualquer outro comando não ira funcionar !")