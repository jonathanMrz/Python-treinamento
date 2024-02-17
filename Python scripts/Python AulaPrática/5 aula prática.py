fatiado="Bolo de cenoura"

print(fatiado[0:15:2], len(fatiado))

faca=fatiado.count("o",0,15)
print(faca)

separed= fatiado.split()
print("{0} {1} {2}".format(separed[1], separed[0], separed[2]))

print("vem até aonde estou, vem até aonde eu irei, vem até aonde fui, vem até mim".count("vem"))
print("vem até aonde estou, vem até aonde eu irei, vem até aonde fui, vem até mim".replace("vem","bola"))
print("vem até aonde estou, vem até aonde eu irei, vem até aonde fui, vem até mim".find("vem"))
print("vem até aonde estou, vem até aonde eu irei, vem até aonde fui, vem até mim".upper())
print("vem até aonde estou, vem até aonde eu irei, vem até aonde fui, vem até mim".upper().count("VEM"))
#observação, o print é colocado como uma semi-"variável" neste caso

usemail=str(input("Digite seu E-mail:").strip())
if "@gmail.com" in usemail:
    print("Seu E-mail é {0} certo?".format(usemail))
else:
    print("Seu E-mail é invalido")