#Exercício final do primeiro mundo
dic={"Clean":"\033[m",
    "Pergunta":"\033[1;33m",
    "Resposta":"\033[7;40m"}
#Primeiro exercício
nm1=int(input("{0}Digite o primeiro número: {1}".format(dic["Pergunta"],dic["Clean"])))
nm2=int(input("{0}Digite o segundo número: {1}".format(dic["Pergunta"],dic["Clean"])))
sm=nm1+nm2
print("{0}A soma entre {2} e {3} é igual a {4} {1}".format(dic["Resposta"],dic["Clean"],nm1,nm2,sm))
#Segundo exercício
item=input("{0}Digite o objeto que quer verificar: {1}".format(dic["Pergunta"],dic["Clean"]))
print("{0}O tipo primitivo desse item é: {1}".format(dic["Pergunta"],dic["Clean"]), type(item))
print("{0}O item é um número? {1}".format(dic["Pergunta"],dic["Clean"]), item.isnumeric())
print("{0}O item é alfabetica? {1}".format(dic["Pergunta"],dic["Clean"]), item.isalpha())
print("{0}O item é alfabetico ou numerico?{1}".format(dic["Pergunta"],dic["Clean"]), item.isalnum())
print("{0}O item é espaço? {1}".format(dic["Pergunta"],dic["Clean"]), item.isspace())
print("{0}O item esta maiusculo? {1}".format(dic["Pergunta"],dic["Clean"]), item.isupper())
print("{0}O item esta minusculo? {1}".format(dic["Pergunta"],dic["Clean"]), item.islower())