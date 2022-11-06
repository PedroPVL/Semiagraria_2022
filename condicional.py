#As condicionais permitem que o algoritmo tenha estrutura lógica
#Por exemplo vamos dizer que este algoritmo define se com sua média final você estara apto a passar de ano, ir pra recuperação ou reprovar

nota = float(input("Digite aqui sua nota: "))

if nota>=0 and nota<=4:
    print("Aluno reprovado")
else:
    print("Nota invalida")
if nota>4 and nota<7:
    print("Aluno elegível a recuperação")
if nota>= 7:
    print("Aluno aprovado")
