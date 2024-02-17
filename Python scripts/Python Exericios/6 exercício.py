import random as rd
#Primeiro exercício
pcnm= rd.randint(0,5)
psnm=int(input("Escolha um número entre 0 e 5: "))
if pcnm==psnm:
    print("Parabens, você ganhou, o número escolhido pelo pc foi o mesmo escolhido por você")
else:
    print("Infelizmente você perdeu, o número escolhido pelo pc foi diferente do escolhido por você")
#Segundo exercício
carvl=int(input("Digite a velocidade de seu carro em km/h: "))
if carvl>=80:
    print("Infelizmente você ultrapassou a velocidade permetida, você ira receber uma multa de {0} reais.".format((carvl-80)*7))
else:
    print("Felizmente você está dentro da velocidade permitida, pode continuar a viagem.")
#Terceiro exercício
nm1=int(input("Digite um número: "))
if nm1%2 ==0 :
    print("Par")
else:
    print("Impar")
#Quarta questão
km1=float(input("Quantos Km serão percorridos na viagem? "))
if km1<=200:
    print("Sua viajem custara {:.2f} reais".format(km1*0.50))
else:
    print("Sua viajem custara {:.2f} reais".format(km1*0.45))
#Quinta questão
ano=int(input("Digite um ano: "))
if ano%4==0:
    print("O ano {} é um ano Bissexto".format(ano))
else:
    print("O ano {} não é um ano Bissexto".format(ano))
#Sexta questão
a=int(input("Digite o número A: "))
b=int(input("Digite o número B: "))
c=int(input("Digite o número C: "))
if a<b and a<c:
    print("Menor: A")
    if b>c:
        print("Maior: B")
    else:
        print("Maior: C")
if b<a and b<c:
    print("Menor: B")
    if a>c:
        print("Maior: A")
    else:
        print("Maior: C")
if c<a and c<b:
    print("Menor: C")
    if a>b:
        print("Maior: A")
    else:
        print("Maior: B")
#Sétima questão
sal=float(input("Digite seu salário: "))
if sal>=1250.00:
    print("Seu novo salário é de {}".format((sal*10)/100+sal))
else:
    print("Seu novo salário é de {}".format((sal*15/100+sal)))
#Oitava questão
r1=int(input("Digite o valor da primeira reta: "))
r2=int(input("Digite o valor da segunda reta: "))
r3=int(input("Digite o valor da terceira reta: "))
if r1+r2>r3 and r2+r3>r1 and r1+r3>r2:
    print("Essas 3 retas podem sim formar um triangulo!")
else:
    print("Essas 3 retas não podem formar um triangulo.")