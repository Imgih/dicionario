cadastro = {}

while True:
    nome = input("Digite o seu nome: ")
    if nome == '':
        break
    
    idade = int(input("Digite a sua idade: "))
    cidade = input("Digite a sua cidade: ")
    
    #adiciona os dados ao dicionário
    cadastro[nome] = {"idade": idade, "cidade": cidade}

#imprime o cadastro completo
print("Cadastro: ")
print(cadastro)

for nome, dados in cadastro.items():
    print("- Nome: ", nome)
    print(" Idade:", dados["idade"])
    print(" Cidade:", dados["cidade"])
