#Primeiro exercício
nm1=str(input("Qual o seu nome completo? ")).strip()
nm1div=nm1.split()
print("{0}\n{1}".format(nm1.upper(),nm1.lower()))
print("Seu nome completo tem {} letras\nSeu primeiro nome tem {} letras".format(len(nm1)-nm1.count(" "),len(nm1div[0])))
#Segundo exercício
num1=str(input("Digite um número: "))
print("Unidade:{0}\nDezena:{1}\nCentena:{2}\nMilhar{3}".format(int(num1[3]),int(num1[2]),int(num1[1]),int(num1[0])))
#Terceiro exercício
citnm=str((input("Digite o nome de sua cidade: ")).strip().upper())
print("SANTO" in citnm[0:5])
#Quarto exercício
nm2=str((input("Qual o seu nome completo? ")).upper().strip())
print("SILVA" in nm2)
#Quinto exercício
frase1=str(input("Digite uma frase: "))
print('a letra "A" aparece {0} vezes, ela aparece pela primeira vez em {1}, e pela ultima vez em {2}'.format(frase1.count("A"),frase1.find("A"), frase1.rfind("A")))
#Sexto exercício
nm3=str((input("Digite seu nome completo: ")).strip())
nm3div=nm3.split()
print("Seu primeiro nome é {}, e seu ultimo sobrenome é {}".format(nm3div[0],nm3div[-1]))