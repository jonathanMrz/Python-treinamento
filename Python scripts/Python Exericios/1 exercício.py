#Exercício final do primeiro mundo
dic={"Clean":"\033[m",
    "Pergunta":"\033[1;33m",
    "Resposta":"\033[7;40m"}
#Primeiro exercício
nome= input("{0}Qual seu nome? {1}".format(dic["Pergunta"],dic["Clean"]))
print("{1}Bem vindo(a) {0} {2}".format(nome,dic["Resposta"],dic["Clean"]))
#Segundo exercício
dia= input("{0}Qual dia você nasceu? {1}".format(dic["Pergunta"],dic["Clean"]))
mes= input("{0}Qual mês você nasceu? {1}".format(dic["Pergunta"],dic["Clean"]))
ano= input("{0}Qual ano você nasceu? {1}".format(dic["Pergunta"],dic["Clean"]))
print("{0}Você nasceu em {2}/{3}/{4} {1}".format(dic["Resposta"],dic["Clean"],dia,mes,ano))
#Terceiro exercício
numero1= input("{0}primeiro número: {1}".format(dic["Pergunta"],dic["Clean"]))
numero2= input("{0}segundo número: {1}".format(dic["Pergunta"],dic["Clean"]))
soma= int(numero1)+int(numero2)
print("{0}{2} {1}".format(dic["Resposta"],dic["Clean"],soma))