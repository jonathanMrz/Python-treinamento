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
#Quinta questão[=================================================================]
#Sexta questão[==================================================================]