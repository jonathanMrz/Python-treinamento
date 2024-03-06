#Primeira questão[===============================================================]
#Segunda questão[================================================================]
#Terceira questão[===============================================================]
#Quarta questão[=================================================================]
#Quinta questão[=================================================================]
#Somente para fazer exercícios muito longos de forma separada
timesfut=("Flamengo","Palmeiras","São Paulo","Athletico Paranaence","Atlético Mineiro","Corinthians","Fluminense","Grêmio","Fortaleza","América Mineiro","Internacional","Santos","Bahia","Botafogo","Red Bull Bragantino","Atlético Goianiense","Cruzeiro","Ceará","Cuiabá","Goiás")
print(f"Os cinco primeiros colocados {timesfut[0:5]}")
print(f"Os quatro ultimos colocados {timesfut[-1:-5:-1]}")
print(f"Em ordem alfabética: \n{sorted(timesfut)}")
print(f"Posição do time Corinthians: {(timesfut.index("Corinthians"))+1}º lugar")