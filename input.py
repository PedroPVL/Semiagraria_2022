#a função input permite que o usuário interaja diretamente com valores do algoritmo

a = input("Digite seu nome aqui: ")

print("Seu nome é:", a)

#porém uma das fraquezas do input é que ele só retorna valores em formato de texto(string)

print("Tipo númerico da função input", type(a))
#então para realizar calculos com input do usuário teremos que forçar o tipo na função(typecasting)

int = int(input("Digita um número para elevalo a segunda potência: "))
int = int**2

print("Resultado:", int)