n1=int(input("Digite um valor: "))
n2=int(input("Digite outro valor: "))
sm=n1+n2
print("A soma entre",n1,"e",n2,"vale",sm)
#Outro caminho com maior simplicidade
print("A soma entre {0} e {1} vale {2}".format(n1,n2,sm))
import math
n3= math.pow(n1,n2)
print(n3)