import random
print("Hello World")

#Crie um número aleatório
numero = random.randint(1,10)
print (numero)

#crie dois números aleatórios e diga a soma deles
numero1 = random.randint(1,10)
numero2 = random.randint(1,10)
print (numero1)
print (numero2)
print (numero1 + numero2)

#Crie um programa que peça as 4 notas bimestrais e mostre a média
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
nota4 = int(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4)/4
print ("A média é: {:.1f}".format(media))

#Crie um programa que converta metros para centímetros
metros = int(input("Digite o valor em metros: "))
centimetros = metros * 100
print ("O valor em centímetros é: ", centimetros)

#Crie um programa que peça o raio de um círculo, calcule e mostre sua área
raio = int(input("Digite o raio do círculo: "))
area = 3.14 * (raio ** 2)
print ("A área do círculo é: ", area)

#Crie um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário
lado = int(input("Digite o valor do lado do quadrado: "))
area = lado ** 2
print ("A área do quadrado é: ", area)
print ("O dobro da área do quadrado é: ", area * 2)

#Crie um programa que pergunte quanto você ganha por hora e o número de horas trablhadas no mês. Calcule e mostre o total do seu salário no referido mês
ganho = int(input("Digite quanto você ganha por hora: "))
horas = int(input("Digite quantas horas você trabalha por mês: "))
salario = ganho * horas
print ("O seu salário é: ", salario)

#Crie um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius
fahrenheit = int(input("Digite a temperatura em Fahrenheit: "))
celsius = (fahrenheit - 32) / 1.8
print ("A temperatura em Celsius é: ", celsius)

#Crie um programa que peça a temperatura em graus Celsius, transforme e mostre a temperatura em graus fahrenheit
celsius = int(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 1.8) + 32
print ("A temperatura em Fahrenheit é: ", fahrenheit)