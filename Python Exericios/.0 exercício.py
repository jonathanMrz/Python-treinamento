#Primeira questão[===============================================================]
#Segunda questão[================================================================]
#Terceira questão[===============================================================]
#Quarta questão[=================================================================]
#Quinta questão[=================================================================]
#Sexta questão[==================================================================]
#Somente para fazer exercícios muito longos de forma separado
list_ex3=[]
list_usv2=["S"]
while list_usv2[0] in "S":
    try:
        list_ex3.append(int(input("Digite um valor: ")))
    except:
        print("Digite um valor válido!")
    print("-="*20)
    list_usv2=input("Deseja continuar? ")[0].strip().upper()
    if list_usv2[0] not in "SN":
        print("Digite um valor válido!")
        list_usv2=input("Deseja continuar? ")[0].strip().upper()