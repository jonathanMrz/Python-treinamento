#primeiro exercício
n=int(input("Digite o valor: "))
ant=n-1
suc=n+1
print("O número {0}\nSeu antecessor {1}\nSeu sucessor {2}".format(n,ant,suc))
#primeiro exercício/ outro caminho sem precisar criar os objetos "ant" e "suc"
print("O número {0}\nSeu antecessor {1}\nSeu sucessor {2}".format(n,n-1,n+1))
#segundo exercício
n1=int(input("Digite o valor: "))
n1d= n1*2
n1t= n1*3
n1q= n1**(1/2)
print("O número {0}\nSeu dobro {1}\nSeu triplo 5{2}\nSua raiz {3}".format(n1,n1d,n1t,n1q))
#segundo exercício/ outro caminho sem precisar criar os objetos "n1d","n1t","n1q"
print("O número {0}\nSeu dobro {1}\nSeu triplo {2}\nSua raiz {3}".format(n1,n1*2,n1*3,n1**(1/2)))
#terceiro exercício
nota1=int(input("Primeira nota do aluno: "))
nota2=int(input("Segunda nota do aluno: "))
media= (nota1+nota2)/2
print("Primeira nota {0}\nSegunda nota {1}\nMédia {2}".format(nota1,nota2,int(media)))
#quarto exercício
metros=int(input("Digite quantos metros são: "))
centimetros=metros*100
milimetros=centimetros*10
print("Distancia em metros {0}\nDistancia em centimetros {1}\nDistancia em milimetros {2}".format(metros,centimetros,milimetros))
#quinto exercício
n2=int(input("Digite o número que será colocado em tabuada:"))
print("Tabuada de {0}\n{0}x1={1}\n{0}x2={2}\n{0}x3={3}\n{0}x4={4}\n{0}x5={5}\n{0}x6={6}\n{0}x7={7}\n{0}x8={8}\n{0}x9={9}\n{0}x10={10}".format(n2,n2*1,n2*2,n2*3,n2*4,n2*5,n2*6,n2*7,n2*8,n2*9,n2*10))
#sexto exercício
real=float(input("Quantos reais você tem na carteira? "))
dollar=float(3.27)
print("Você tem {0} reais, cada dolar vale {1}, você consegue comprar {2:.2f} dolares".format(real,dollar,real/dollar))
#sétimo exercício
alt=float(input("Qual a altura da parede? "))
lar=float(input("Qual a largura da parede? "))
area=float(alt*lar)
print("Sua parede tem uma área de {0:.2f} para pintalá inteira ira custar {1:.2f} litros de tinta".format(area,area/2))
#oitavo exercício
prod=int(input("Insira o preço original do produto: "))
print("O preço original do produto é {0}, com o desconto fica {1}".format(prod,int(prod-(prod*5)/100)))
#nono exercício
sal=float(input("Qual o salário do funcionario? "))
salaument= sal+(sal*15)/100
print("Salário do funcionário antes do aumento {0}\nSalário do funcionário depois do aumento {1}".format(sal,salaument))