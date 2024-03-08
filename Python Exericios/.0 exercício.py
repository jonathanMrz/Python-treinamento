#Primeira questão[===============================================================]
#Segunda questão[================================================================]
#Terceira questão[===============================================================]
#Quarta questão[=================================================================]
#Quinta questão[=================================================================]
#Sexta questão[==================================================================]
#Somente para fazer exercícios muito longos de forma separada
cnt=objeto=valor=0
while True:
    objeto=input("Digite o nome de um produto: ").strip()
    valor=int(input("Digite o valor deste produto: "))
    cnt=input("[S/N]Deseja adcionar mais um valor? ").strip().upper()
    while cnt not in "SN":
        print("Digite um valor valido!")
        cnt=input("[S/N]Deseja adicionar mais um valor? ").strip().upper()
        if cnt in "SN":
            break
    if cnt in "Nn":
        break
lista=("Caneta",1.50,"Borracha",0.75,"Lapiz",1.00)

for pos in range(0,len(lista)):
    if pos%2==0:
        print(f"{lista[pos]:.<30}",end=" ")
    else:
        print(f"R${lista[pos]:<30}")