nome=input("Digite o seu nome:")

idade=int(input("Digite a sua idade, por favor:"))

if idade>80: print(nome,", como você está quase um fóssil pré-histórico!!!")
else:
    if idade>50:
        print(nome,", você é uma pessoa quase velha kkkk!!!")
        print("Quase velha? Quantas pessoas de",idade*2,"anos você conhece?")
    else:
        if idade>18:
            print(nome,", você é uma com ",idade,"anos de idade (óbvio)")
        else: print(nome," quase a idade de um bebê!!")