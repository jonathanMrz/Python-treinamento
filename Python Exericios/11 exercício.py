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
#Sexta questão[==================================================================]