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

#Terceira questão[===============================================================]
#Quarta questão[=================================================================]
#Quinta questão[=================================================================]
