votos = {}

while True:
    candidato = input("Digite o nome do candidato (ou fim para encerar): ")
    if candidato == 'fim':
        break 
    
    #verifica se o candidato já recebeu votos antes
    if candidato in votos:
        votos[candidato] +=1
    else:
        votos[candidato] = 1
    
 #imprime o resultado da votação
print("Resultado da votação: ")
for candidato, quantidade in votos.items():
    print(candidato, "-", quantidade, 'votos')
     
print(votos)
    