#Somente para fazer exercícios muito longos de forma separada
nm0=cnt0=pmc=""
preco0=soma=mqm=pdmc=0
while True:
    nm0=str(input("Escreva o nome do produto: "))
    preco0=int(input("Informe o preço do produto: "))
    if preco0>1000:
        mqm+=1
    if soma==0 or preco0 > pdmc:
        pmc=nm0
        pdmc=preco0
    soma+=preco0
    cnt0=str(input("[S/N]Quer adicionar mais um produto? ")).strip()
    while cnt0 not in "SsNn":
        print("Digite uma resposta valida.")
        cnt0=str(input("[S/N]Quer adicionar mais um produto? ")).strip()
        if cnt0 in "Nn":
            break
    if cnt0 in "Nn":
        break
print(f"A soma de todos produtos: {soma}\nQuantidade de produtos com o preço acima de 1000: {mqm}\nProduto mais caro: {pmc}")