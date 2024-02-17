import math
import random
import pygame
#Sexta questão
pygame.init()
pygame.mixer.music.load("Objetos/crystallstest.mp3")
pygame.mixer.music.play()
#Primeira questão
num1=float(input("Digite um valor quebrado: "))
print("O valor sem os números depois do ponto é: {0}".format(math.trunc(num1)))
#Segunda questão
co=float(input("Digite o cateto oposto: "))
ca=float(input("Digite o cateto adjacente: "))
hi=float(math.hypot(co,ca))
print("O cateto oposto é {0}, o adjacente é {1} e a hipotenusa é {2}".format(co,ca,hi))
#Terceira questão
ang=int(input("Digite um ângulo para ver seu cosseno, seno e tangente: "))
cos=math.cos(math.radians(ang))
seno=math.sin(math.radians(ang))
tang=math.tan(math.radians(ang))
print("O angulo é {0}\nSeu cosseno é {1:.2f}\nSeu seno é {2:.2f}\nE a tangente é {3:.2f}".format(ang,cos,seno,tang))
#Quarta e quinta questão
alun1=str(input("Primeiro aluno: "))
alun2=str(input("Segundo aluno: "))
alun3=str(input("Terceiro aluno: "))
alun4=str(input("Quarto aluno: "))
lista1=[alun1,alun2,alun3,alun4]
random.shuffle(lista1)
print("O aluno escolhido para limpar o quadro foi o {0}".format(random.choice(lista1)))
print("A ordem de apresentação do trabalho é {0}".format(lista1))