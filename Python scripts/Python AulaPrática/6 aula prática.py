tempo=int(input("Quantos anos tem seu carro? "))
#forma inteira; Obs: o python diferentemente de algumas linguagens, no if e no else se coloca ":" no final
if tempo<=3:
    print("Carro novo")
else:
    print("Carro velho")
#forma simplificada
print("Carro novo"if tempo<=3 else "Carro velho")
#testes
nmc=str((input("Qual o seu nome e seu primeiro sobrenome? ")).strip())
pnm=nmc.split()
if len(pnm[0])>=8:
    if len(pnm[1])>=8:
        print("O death note nunca será um problema")
    else:
        print("O death note pode te matar, mas com um pouco de dificuldade")
else:
    if len(pnm[1])>=8:
        print("O death note pode te matar, mas com um pouco de dificuldade")
    else:
        print("Você esta totalemtne suscetível ao death note, tome cuidado!")
print("Mas deixando isto de lado, bem vindo {}".format(pnm[0]))
#test de nota
nt1=float(input("Digite sua primeira nota: "))
nt2=float(input("Digite sua segunda nota: "))
md=(nt1+nt2)/2
if nt1>=5:
    print("Parabens, sua primeira nota {:.2f} está dentro do nescessário para passar!".format(nt1))
    if nt2>=5:
        print("Parabens, sua segunda nota {:.2f} está dentro do nescessário para passar!".format(nt2))
    else:
        print("Infelizmente sua segunda nota {:.2f} não está dentro do nescessário para passar".format(nt2))
else:
    print("Infelizmente sua primeira nota {:.2f} não esta dentro do nescessário para passar".format(nt1))
    if nt2>=5:
        print("Parabens, sua segunda nota {:.2f} está dentro do nescessário para passar!".format(nt2))
    else:
        print("Infelizmente sua segunda nota {:.2f} não está dentro do nescessário para passar".format(nt2))
print("Sua média final é {:.2f},".format(md),"parabens,você passou!"if md>=5 else"infelizmente você não passou")