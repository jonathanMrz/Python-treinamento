import time as tm
import datetime as dt
#Primeira questão
for fogoscontagem in range(10,0,-1):
    print(fogoscontagem)
    tm.sleep(1)
print("*OS FOGOS DE ARTIFICIOS SÃO ACIONADOS*")
#Segunda questão[================================================================]
for par in range(1,51):
    if par%2==0:
        print(par)
    else:
        " "
#Terceira questão[===============================================================]
imp=0
for imparmthree in range(1,501):
    if imparmthree%2==0:
        ""
    elif imparmthree%3==0:
        nat = imparmthree
        print(imparmthree)
        imp+=nat
print("A soma de todos multiplos de 3 que não são par até 500 é igual a :{}".format(imp))
#Quarta questão[==================================================================]
num1=int(input("Digite o valor que vai ser usado na tabuada: "))
for l in range(1,10):
    print("{}x{}={}".format(num1,l,num1*l))
#Quinta questão[==================================================================]
soma6=0
for topz in range(1,7):
    v=int(input("({0}/6) Digite um valor: ".format(topz)))
    if v%2==0:
        soma6+=v
print("Soma de todos valores pares digitados: {0}".format(soma6))
#Sexta questão[==================================================================]
listarz=[]
Pvl=int(input("Primeiro termo da PA: "))
Rz=int(input("Razão da PA: "))
for pgf in range(0,10):
    print("{}".format(Pvl))
    listarz.append(Pvl)
    Pvl+=Rz
print("Os 10 primeiros valores desta PG criada são:\n{}".format(listarz[:10]))
#Sétima questão[=================================================================]
number=int(input("Digite um número: "))
TstP=0
for plp in range(1,(number+1)):
    if number%plp==0:
        TstP+=1
if TstP==2:
    print("Primo")
elif TstP>2 or TstP==1:
    print("Não é primo")
#Oitava questão[=================================================================]
f=input("Digite uma frase: ").upper().strip().split()
tf="".join(f)
inv=tf[::-1]
print("O inverso de {} é {}".format(tf,inv))
if inv==tf:
    print("Isto é um polídroma!")
else:
    print("Isto não é um polídroma.....")
#Nona questão[===================================================================]
anoat=dt.datetime.today().year
quantMa=0
quantMe=0
for nasc in range(0,7):
    ano1=int(input("Digite o ano que você nasceu: "))
    if (anoat-ano1)>=21:
        print("Essa pessoa já tem {} logo ela já é maior de idade".format(anoat-ano1))
        quantMa+=1
    else:
        print("Essa pessoa já tem {} logo ela ainda não é maior de idade".format(anoat-ano1))
        quantMe+=1
print("A quantidade de pessoas maior de idade é: {}".format(quantMa))
print("A quantidade de pessoas menor de idade é: {}".format(quantMe))
#Decima questão[=================================================================]
exlist=[]
for x in range(0,5):
    peso=int(input("Digite seu peso em kg: "))
    exlist.append(peso)
exlist.sort()
print("Dentre os pesos anotados:\nO menor peso:{}\nO maior peso:{}".format(exlist[0],exlist[-1]))
#Decima segunda questão[=========================================================]
somaidade=0
mediaidade=0
maioridadehomem=0
nomevelho=""
totmulher20=0
for loopin in range(1,5):
    print("------------------]{}° Pessoa[---------------------".format(loopin))
    nome=str(input("Digite seu nome: ")).strip()
    idade=int(input("Digite sua idade: "))
    sexo=str(input("Digite seu sexo[M/F]: ")).strip().upper().strip()
    somaidade+=idade
    if loopin ==1 and sexo=="M":
        maioridadehomem=idade
        nomevelho=nome
    if idade>maioridadehomem and sexo=="M":
        maioridadehomem=idade
        nomevelho=nome
    if sexo=="F" and idade<20:
        totmulher20+=1
mediaidade=somaidade/4
print("Média de todas as idades:{}".format(mediaidade))
print("Nome do homem mais velho: {}".format(nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(totmulher20))