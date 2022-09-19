# Calculadora

def num(n, tipo):
    while True:
        while True:
            if tipo == "%":
                print("Qual porcentagem você quer de {:.2f}".format(n))
            else:
                print("Quer {} {:.2f} com qual número?".format(tipo, n))
            try:
                num = float(input("-> "))
                break
            except Exception:
                print("Digite apenas números!\n")
                continue
        match tipo:
            case "dividir":
                if num != 0:
                    break
                else:
                    print("Impossivel dividir por zero!")
                    continue
            case _:
                break

    return num


print("Bem vindo a calculadora!")

while True:
    print("Digite o número desejado!")
    try:
        numero = float(input("-> "))
        break
    except Exception:
        print("Falha ao obter o número")
        print("Digite apenas números\n")
        continue

while True:
    while True:
        print("""Que tipo de operação você quer fazer com {:.2f}?
        Opções:
        Adição -> +
        Subtração -> -
        Multiplicação -> *
        Divisão -> /
        Porcentagem -> %
        Finalizar -> =""".format(numero))
        operacao = input("-> ").strip()
        match operacao:
            case "+" | "-" | "*" | "/" | "%" | "=":
                break
            case _:
                print("Operação não existe!\n")
                continue

    match operacao:
        case "+":
            numero += num(numero, "somar")
        case "-":
            numero -= num(numero, "subtrair")
        case "*":
            numero *= num(numero, "multiplicar")
        case "/":
            numero /= num(numero, "dividir")
        case "%":
            numero *= num(numero, operacao) / 100
        case "=":
            break

print("O resultado final é: {:.2f}".format(numero))
print("*" * 40)
