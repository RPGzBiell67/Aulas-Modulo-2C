def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro: Divisão por zero!"
    else:
        return x / y

print("\033[32mSelecione a operação:")
print("\033[35m1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = input("\033[37mDigite a sua escolha (1/2/3/4): ")

num1 = float(input("\033[30mDigite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if escolha == '1':
    print("\033[32mResultado:", adicao(num1, num2))
elif escolha == '2':
    print("\033[32mResultado:", subtracao(num1, num2))
elif escolha == '3':
    print("\033[32mResultado:", multiplicacao(num1, num2))
elif escolha == '4':
    print("\033[32mResultado:", divisao(num1, num2))
else:
    print("Escolha inválida")
