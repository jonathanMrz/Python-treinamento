#Primeira questão[===============================================================]
list_ex1=[int(input("Digite o Primeiro valor: ")),int(input("Digite o Segundo : ")),int(input("Digite o Terceiro valor: ")),
int(input("Digite o Quarto valor: ")),int(input("Digite o Quinto valor: "))]
print(f"""[P:{list_ex1.index(max(list_ex1))}]O maior valor da lista é: {max(list_ex1)}
[P:{list_ex1.index(min(list_ex1))}]O menor valor da lista é: {min(list_ex1)}""")
#Segunda questão[================================================================]
list_ex2=[];list_usv1=["S",0]
while list_usv1[0] in "S":
    print("Adicione um número a lista"if len(list_ex2)==0 else"Adicione mais um número a lista.")
    list_usv1[1]=int(input("valor:"))
    while list_usv1[1] in list_ex2:
        print("Valor repetido, escreva outro.")
        list_usv1[1]=int(input("valor:"))
    list_ex2.append(list_usv1[1])
    list_usv1[0]=input("[S/N]Deseja adicionar mais um valor? ").upper().strip()
    while list_usv1[0] not in "SN":
        print("Digite um valro válido![Sim ou Não]")
        list_usv1[0]=input("[S/N]Deseja adicionar mais um valor? ").upper().strip()
print(sorted(list_ex2))
#Terceira questão[===============================================================]
lista = list()
for c in range(5):
    n = int(input("Digite o numero: "))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        for pos, x in enumerate(lista):
            if n <= x:
                lista.insert(pos, n)
                break
print(lista)
#Quarta questão[=================================================================]
list_ex3=[]
list_usv2=["S"]
while list_usv2[0] in "S":
    while True:
        try:
            list_ex3.append(int(input("Digite um valor: ")))
            break
        except:
            print("Digite um valor válido!")
    print("-="*20)
    list_usv2=input("[S/N]Deseja continuar? ")[0].strip().upper()
    while list_usv2[0] not in "SN":
        print("Digite um valor válido!")
        list_usv2=input("[S/N]Deseja continuar? ")[0].strip().upper()
print("-="*20)
list_ex3.sort(reverse=True)
print(f"Os números digitados: {list_ex3}\nA quantidade de números nele: {len(list_ex3)}")
for c in range(0,list_ex3.count(5)):
    if c==0:
        print(f"O número cinco aparece {list_ex3.count(5)} vez na posição: "if list_ex3.count(5)==1
        else f"O número cinco aparece {list_ex3.count(5)} vezes nas posições: ", end="")
    print(list_ex3.index(5)+c,end=" ")
#Quinta questão[=================================================================]
list_main=[];list_imp=[];list_par=[];list_usv3=["S",0]
while list_usv3[0] in "S":
    list_main.append(int(input("Digite um número: ")))
    if list_main[list_usv3[1]]%2==0:
        list_par.append(list_main[list_usv3[1]])
    elif list_main[list_usv3[1]]%2!=0:
        list_imp.append(list_main[list_usv3[1]])
    list_usv3[1]+=1
    list_usv3[0]=input("Deseja continuar?").strip().upper()
    while list_usv3[0][0] not in "SN":
        print("Digite um valor válido!")
        list_usv3[0]=input("Deseja continuar?").strip().upper()
list_main.sort();list_par.sort();list_imp.sort()
print(f"Lista principal: {list_main}\n-Lista de números par: {list_par}\n-Lista de números impar: {list_imp}")
#Sexta questão[==================================================================]
list_usv4=[];list_ex4=[]
list_ex4.append(input("Digite uma operação númerica: "))
list_usv4.append(list_ex4[0].count("(")-list_ex4[0].count(")"))
if list_ex4[0].count("(")==list_ex4[0].count(")"):
    print("A operação está certa!")
while list_ex4[0].count("(")!=list_ex4[0].count(")"):
    print("A operação está errada")
    print(f"Você esqueceu de colocar", 
        f"{list_usv4[0]} ')'" if list_ex4[0].count("(")>list_ex4[0].count(")") else f"{list_usv4[0]*-1}'('",
        "refaça a operação:")
    list_ex4[0]=input("Digite uma operação númerica:")