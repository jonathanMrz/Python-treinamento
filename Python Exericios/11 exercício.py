import random as rd
#Primeira questão[===============================================================]
extenso=("Zero","Um","Dois","Três","Quatro","Cinco","Seis","Sete","Oito","Nove","Dez","Onze","Doze","Treze","Quatoze","Dezesseis","Dezessete","Dizoito","Dezenove","Vinte")
valornum=int(input("Digite um valor de 0 até 20: "))
if valornum <= 20 and valornum >= 0:
    print(f"Você digitou o número {extenso[valornum]}")
else:
    while valornum>20 or valornum<0:
        print("Digite um valor válido")
        valornum=int(input("Digite um valor de 0 até 20: "))
    print(f"Você digitou o número {extenso[valornum]}")
#Segunda questão[================================================================]
timesfut=("Flamengo","Palmeiras","São Paulo","Athletico Paranaence","Atlético Mineiro","Corinthians","Fluminense","Grêmio","Fortaleza","América Mineiro","Internacional","Santos","Bahia","Botafogo","Red Bull Bragantino","Atlético Goianiense","Cruzeiro","Ceará","Cuiabá","Goiás")
print(f"Os cinco primeiros colocados {timesfut[0:5]}")
print(f"Os quatro ultimos colocados {timesfut[-1:-5:-1]}")
print(f"Em ordem alfabética: \n{sorted(timesfut)}")
print("Posição do time Corinthians: {}º lugar".format((timesfut.index("Corinthians"))+1))
#Terceira questão[===============================================================]
import random as rd
numtupla=(rd.randint(0,20),
        rd.randint(0,20),
        rd.randint(0,20),
        rd.randint(0,20),
        rd.randint(0,20))
print(numtupla)
print(f"Maior valor randomizado: {max(numtupla)}\nMenor valor randomizado: {min(numtupla)}")
#Quarta questão[=================================================================]
snumlist=((int(input("Digite um valor: "))),
    (int(input("Digite um valor: "))),
    (int(input("Digite um valor: "))),
    (int(input("Digite um valor: "))))
if 9 in snumlist:
    print(f"O número nove foi digitado {snumlist.count(9)} vezes")
if 3 in snumlist:
    print(f"O número 3 aparece pela primeira vez na posição {snumlist.index(3)}")
print("Valores pares: ",end="")
for n in snumlist:
    if n%2==0:
        print(n,end=" ")
#Quinta questão[=================================================================]
nv=oq=cnt=objeto=valor=0
lista=[]
while True:
    print("=-"*30)
    objeto=input("Digite o nome de um produto: ").strip()
    valor=float(input("Digite o valor deste produto: "))
    lista.append(objeto);lista.append(valor)
    print("=-"*30)
    cnt=input("[S/N]Deseja adcionar mais um valor?\nResposta: ").strip().upper()
    while cnt[0] not in "SN":
        print("Digite um valor valido!")
        cnt=input("[S/N]Deseja adicionar mais um valor?\nResposta: ").strip().upper()
        if cnt[0] in "SN":
            break
    if cnt[0] in "N":
        break
print("=-"*30)
cnt=input("[S/N]Deseja alterar algo da lista?\nResposta: ").upper().strip()
while cnt[0] not in "SN":
    print("Digite um valor válido!")
    cnt=input("[S/N]Deseja alterar algo da lista?\nResposta: ").upper().strip()
    if cnt[0] in "SN":
        break
print("=-"*30)
while cnt[0] in "S":
    for alt in range(0,len(lista)):
        if alt%2==0:
            print(f"[{lista.index(lista[alt])}] {lista[alt]:.<30}",end=" ")
        else:
            print(f"R${lista[alt]}")
    oq=int(input("Digite o valor do produto que deseja alterar: "))
    print("=-"*30)
    print(f"{lista[oq]:.<30}R${lista[oq+1]}")
    nv=int(input("""Digite oque deseja fazer:
    [0]Para mudar o nome
    [1]Para mudar o valor
    [2]Para deletar
Resposta:"""))
    print("=-"*30)
    if nv==0:
        lista[oq]=input("Digite o novo nome do produto: ")
    elif nv==1:
        lista[oq+1]=float(input("Digite o novo valor do produto: "))
    elif nv==2:
        del(lista[oq+1]);del(lista[oq])
    print("=-"*30)
    cnt=input("[S/N]Deseja alterar algo da lista?\nResposta: ").upper().strip()
    while cnt[0] not in "SN":
        print("Digite um valor válido!")
        cnt=input("[S/N]Deseja alterar algo da lista?\nResposta: ").upper().strip()
        if cnt[0] in "SN":
            break
    if cnt[0] in "N":
        break
print("=-"*30)
for pos in range(0,len(lista)):
    if pos%2==0:
        print(f"{lista[pos]:.<30}",end="")
    else:
        print(f"R${lista[pos]}")
#Sexta questão[==================================================================]