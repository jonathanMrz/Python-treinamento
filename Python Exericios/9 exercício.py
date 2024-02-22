dic={"Clean":"\033[m",
    "Error":"\033[;31m",
    "Amarelo":"\033[;33m"}
import random as rd
#Primeira questão[===============================================================]
sx=input("[M/F]Digite seu sexo: ").strip()[0]
while sx not in "MmFf":
    print("{}Digite um valor válido;{}".format(dic["Error"], dic["Clean"]))
    sx=input("[M/F]Digite seu sexo: ").strip()[0]
print("Seu sexo é {}".format(sx))
#Segunda questão[================================================================]
opcoes=[0,1,2,3,4,5,6,7,8,9,10]
compuiter=int(rd.choice(opcoes))
print("O computador escolheu um número de 0 até 10, e caso você o acerte, você ganha.")
player=int(input("[0~10]Digite um valor:"))
tentativas=1
print(compuiter)
while player!=compuiter:
    print("{}Tente de novo{}".format(dic["Amarelo"],dic["Clean"]))
    player=int(input("[0~10]Digite um valor:"))
    tentativas+=1
print("Parabens, você acertou o número, foi necessário {} tentativa(s)".format(tentativas))
#Terceira questão[===============================================================]
vl1=int(input("Digite um número: "))
vl2=int(input("Digite ou número: "))
selecao=0
while selecao!=5:
    print("[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa")
    selecao=int(input("Digite sua escolha: "))
    if selecao==1:
        print("{}+{}={}".format(vl1,vl2,vl1+vl2))
    elif selecao==2:
        print("{}x{}={}".format(vl1,vl2,vl1*vl2))
    elif selecao==3:
        if vl1>vl2:
            print("{} é o maior número entre os dois.".format(vl1))
        elif vl2>vl1:
            print("{} é o maior número entre os dois.".format(vl2))
        else:
            print("Ambos possuem o mesmo valor.")
    elif selecao==4:
        vl1=int(input("Digite um número: "))
        vl2=int(input("Digite ou número: "))
#Quarta questão[=================================================================]
nm=int(input("Digite um número: "))
nm2=1
while nm!=0:
    nm2*=nm
    nm-=1
print(nm2)
#Quinta questão[=================================================================]
pv=int(input("Digite o primeiro valor: "))
rz=int(input("Digite o valor da razão: "))
cn=10
while cn!=0:
    print(pv)
    pv+=rz
    cn-=1
continuar=str(input("Quer continuar?[Y/N]")).upper().strip()
if continuar in "Y":
    cn=int(input("Quer mais quantos números da pg? "))
    while cn!=0:
        print(pv)
        pv+=rz
        cn-=1
else:
    print("Fim da progressão")
#Sexta questão[==================================================================]
valour1=int(input("Primeiro número da sequência fibonacci: "))
valour2=valour1-1
count=int(input("Até aonde ela vai? "))
while count!=0:
    valour1=valour1+valour2
    print(valour2)
    valour2=valour1+valour2
    print(valour1)
    count-=1
#Sétima questão[=================================================================]
ni=0
contagem=0
soma=0
while ni!=999:
    ni=int(input("[999=end]Digite um número: "))
    if ni==999:
        print("Fim do programa.")
    elif ni!=999:
        soma+=ni
        contagem+=1
print("Soma de todos os números digitados: {}\nNúmero de valores digitados: {}".format(soma,contagem))
#Oitava questão[=================================================================]
soma=0
nim2=0
listanim=[]
while (input("Continuar? ").strip().upper()) in "Ss":
    nim1=int(input("Digite um valor: "))
    soma+=nim1
    nim2+=1
    listanim.append(nim1)
media=soma/nim2
print("Média dos valores digitados: {:.2f}\nMenor valor:{}\nMaior valor:{}".format(media,min(listanim),max(listanim)))