#FUNÇÃO SEM RETORNO E SEM PARAMETRO
def print_lyrics():
    print("I ain't gonna live forever")
    print("I just want to live while I'm alive")

print_lyrics()

# FUNÇÃO SEM RETORNO E COM PARAMETRO
def boas_vindas(nome):
    print(f"Olá, {nome}!!! Seja bem-vindo!!")

nome_digitado = input("digite seu nome: ")
boas_vindas(nome_digitado)

# FUNÇÃO COM RETORNO E COM PRAMETRO
def soma(num_a, num_b):                           # Declarei a função
    soma = num_a + num_b
    return soma

resultado_soma = soma(17, 22)       # num_a recebe 17 / num_b recebe 22
print(resultado_soma)                            # soma recebe num_a + num_b = 39
