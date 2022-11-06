#Em algumas situações é necessário que uma função seja realizada diversas vezes para alcançar o resultado desejado
#Esse código calculara a media anual baseada na média de 4 bimestres
somatorio = 0
i= 1
while i<=4:
    somatorio+= float(input("Digite sua nota: "))
    i+=1

media = somatorio/4
print("Sua média foi: ", media)