#Cores
cores={"Clean":"\033[m",
    "Pergunta":"\033[1;33m",
    "Resposta":"\033[7;40m"   
}
#Prática if, elif e else
ano=str(input("{0}Em qual ano você nasceu? {1}".format(cores["Pergunta"],cores["Clean"])))
if ano >= "2009":
    print("{0}Você é da geração Z {1}".format(cores["Resposta"],cores["Clean"]))
elif "2000" <= ano < "2009":
    print("{0}Você é da geração Y {1}".format(cores["Resposta"],cores["Clean"]))
elif "1990" <=ano < "2000":
    print("{0}Você é da geração X {1}".format(cores["Resposta"],cores["Clean"]))
elif "1980" <=ano < "1990":
    print("{0}Você é da geração W {1}".format(cores["Pergunta"],cores["Clean"]))
else:
    print("{0}Você é de uma geração anterior a contagem de geração pelo alfabeto {1}".format(cores["Resposta"],cores["Clean"]))