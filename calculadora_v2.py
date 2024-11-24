saida = ''


def adicao(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def multiplicacao(num1, num2):
    return num1 * num2


def divisao(num1, num2):
    if num1 or num2 == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return num1 / num2


def calculadora(num1, num2, operador):
    if operador == '+' or operador.lower() == 'soma':
        resultado = adicao(num1, num2)
    elif operador == '-' or operador.lower() == 'subtracao':
        resultado = subtracao(num1, num2)
    elif operador == '*' or operador.lower() == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operador == '/' or operador.lower() == 'divisao':
        resultado = divisao(num1, num2)
    else:
        resultado = 'operador não válido'
    return resultado


while saida.lower() != 'n':
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    operacao = input(
        'Digite o operador desejado  (+, -, *, / ou o nome): ')
    resultado = calculadora(num1, num2, operacao)

    print(f"Resultado da operação: {resultado}")

    saida = input("Deseja continuar? (S/N): ")

print("Programa encerrado")
