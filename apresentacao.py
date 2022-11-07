print("Bem vindo ao progama de valores")



while True:
    print("Digite o ano de seu veículo: ")

    ano = int(input())

    print("Digite o preço de seu veículo: ")

    preco = float(input())

    if ano<1990 and ano> 1900:
        print("Seu veículo antecede a decada de 90, a taxa de juros aplicada sobre seu valor será de 1% totalizando: ")
        print(preco + (preco*0.01))
        break
    elif ano>=1990 and ano<2022:
        print("Parabéns seu veículo é relativamente novo, a taxa de juros aplicada sobre seu valor será de 1,5% totalizando: ")
        print(preco+(preco*0.015))
        break
    elif ano<=1900:
        print("Data invalida volte e corrija!")





