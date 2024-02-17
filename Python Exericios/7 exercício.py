import datetime
import random as rd
import time as tm
dic={"Clean":"\033[m",
    "Pergunta":"\033[1;33m",
    "Derrota":"\033[3;31m",
    "Vitoria":"\033[3;32m",
    "Empate":"\033[3;37m",
    "BEP":"\033[1;37m",}

#Primeira questão
casa1=float(input("Qual o valor da casa que você deseja comprar? "))
sal1=float(input("Qual o seu salário mensal? "))
anos1=int(input("Durante quantos anos de prestação você vai pagar a casa? "))
if casa1/(12*anos1)<((sal1*30)/100):
    print("Você cosegue compra-lá pagando R${:.2f} todo més durante {} anos".format(casa1/(12*anos1),anos1))
else:
    print("Você não consegue compra-lá, para compra-lá você teria que pagar R${:.2f} todo mês durante {} anos\nMas você só consegue pagar {:.2f} ao mês".format(casa1/(12*anos1),anos1,(sal1*30)/100))

#Segunda questão
num1=int(input("Escreva um número: "))
print("""Escolha uma das opções:
    [0]-Binario
    [1]-Octal
    [2]-Hexadecimal""")
choose=input("Valor escolhido: ")
if choose in "0":
    print(bin(num1))
elif choose in "1":
    print(oct(num1))
elif choose in "2":
    print(hex(num1))
else:
    print("Ensira umvalor válido.")

#Terceira questão
num2=int(input("Escreva o primeiro número: "))
num3=int(input("Escreva o segundo número: "))
if num2>num3:
    print("O primeiro valor {} é maior".format(num2))
elif num3>num2:
    print("O segundo valor {} é maior".format(num3))
else:
    print("Ambos possuem o mesmo valor.")

#Quarta questão
nasc=int(input("Qual ano vocês nasceu? "))
ano1=int(datetime.datetime.today().year)
if(ano1-nasc)==18:
    print("Este é ano de alistamento, cheque o site do exercito e confira.")
elif(ano1-nasc)<18:
    print("Este ainda não é ano de alistamento, falta(m) {} ano(s)".format(18-(ano1-nasc)))
else:
    print("já passou o tempo de se alistar, creio que você tenha se alistado a {} ano(s) atras".format((ano1-nasc)-18))

#Quinta questão
nt1=float(input("Primeira nota: "))
nt2=float(input("Segunda nota: "))
md=(nt1+nt2)/2
if md<5.0:
    print("Reprovado")
elif md>=5.0 and md<7.0:
    print("Recuperação")
else:
    print("Passou")

#Sexta questão
nasc2=int(input("Em qual ano você nasceu? "))
ano2=int(datetime.datetime.today().year)
if (ano2-nasc2)<=9:
    print("Mirim")
elif 9<(ano2-nasc2)<=14:
    print("Infantil")
elif 14<(ano2-nasc2)<=19:
    print("Junior")
elif (ano2-nasc2)==20:
    print("Master")
else:
    print("Master")

#Sétima questão
r1=int(input("Digite o valor da primeira reta: "))
r2=int(input("Digite o valor da segunda reta: "))
r3=int(input("Digite o valor da terceira reta: "))
if r1+r2>r3 and r2+r3>r1 and r1+r3>r2:
    print("Essas 3 retas podem sim formar um triângulo!")
    if r1==r2==r3:
        print("E ele é um Triângulo Equilátero(todos lados iguais)")
    elif r1==r2 or r1==r3 or r2==r3:
        print("E ele é um Triângulo Isôsceles(dois lados iguais)")
    else:
        print("E ele é um Triângulo Escaleno(todos lados diferentes)")
else:
    print("Essas 3 retas não podem formar um triângulo.")

#Oitava questão
peso1=float(input("Digite seu peso: "))
altura1=float(input("Digite sua altura: "))
imc= peso1/(altura1*altura1)
if imc<18.5:
    print("Abaixo do peso")
elif imc>=18.5 and imc<25.0:
    print("Peso ideal")
elif imc>=25.0 and imc<30.0:
    print("Acima do peso")
elif imc>=30.0 and imc<40.0:
    print("Obsidade")
elif imc>=40:
    print("Obsidade morbida")

#Nona questão
preco=float(input("Digite o preço do produto: "))
print("""Tipos de pagamento:
    [0]-À vista/cheque; 10% de desconto é aplicado nesse tipo de pagamento
    [1]-À vista no cartão; 5% de desconto é aplicado nesse tipo de pagamento
    [2]-Em até 2x no cartão; Nenhum desconto é aplicado nesse tipo de pagamento
    [3]-3x ou mais no cartão; Se é adicionado um juros de 20% nesse tipo de pagamento""")
choose1=input("Forma de pagamento escolhido: ")
if choose1=="0":
    print("O valor a ser pago é de R${:.2f} já com os 10% de desconto adicionado".format(preco-(preco*10)/100))
elif choose1=="1":
    print("O valor a ser pago é de R${:.2f} já com os 5% de desconto adicionado".format(preco-(preco*5)/100))
elif choose1=="2":
    print("O valor a ser pago é de {:.2f}".format(preco))
elif choose1=="3":
    print("O valor a ser pago é de {}, já com os juros adiscionados".format(preco+(preco*20)/100))
else:
    print("Escolha uma forma de pagamento valido")

#Decima questão
itens=("Pedra","Papel","Tesoura")
comput=int(rd.randint(0,2))
print("""{0}Escolha um dos valores:
    [0]Pedra
    [1]Papel
    [2]Tesoura{1}""".format(dic["Pergunta"],dic["Clean"]))
player=int(input("{0}Qual vai ser sua jogada? {1}".format(dic["Pergunta"],dic["Clean"])))

tm.sleep(1)
print("{}  JO {}".format(dic["Pergunta"],dic["Clean"]))
tm.sleep(1)
print("{}  KEN {}".format(dic["Pergunta"],dic["Clean"]))
tm.sleep(1)
print("{}  PO!! {}".format(dic["Pergunta"],dic["Clean"]))

print("🏁"* 11)
print("{}A maquina jogou {} {}".format(dic["BEP"],itens[comput],dic["Clean"]))
print("{}O player jogou {} {}".format(dic["BEP"],itens[player],dic["Clean"]))
print("🏁"* 11)

if comput==player:
    print("Resultado: {0}Empate! {1}".format(dic["Empate"],dic["Clean"]))
elif comput==0:
    if player==1:
        print("Resultado: {0}Vitória {1}".format(dic["Vitoria"],dic["Clean"]))
    elif player==2:
        print("Resultado: {0}Derrota..{1}".format(dic["Derrota"],dic["Clean"]))
elif comput==1:
    if player==0:
        print("Resultado: {0}Derrota..{1}".format(dic["Derrota"],dic["Clean"]))
    elif player==2:
        print("Resultado: {0}Vitória! {1}".format(dic["Vitoria"],dic["Clean"]))
elif comput==2:
    if player==0:
        print("Resultado: {0}Vitória! {1}".format(dic["Vitoria"],dic["Clean"]))
    elif player==1:
        print("Resultado: {0}Derrota..{1}".format(dic["Derrota"],dic["Clean"]))
else:
    print("Ensira um valor valido para a jogada.")