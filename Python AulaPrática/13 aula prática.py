regis=[]
pes=[]
mem=[0,0]
while input("[S]Continuar? ")[0].strip().upper() in "S":
    pes.append(input("Digite o nome de uma pessoa: ").strip().title())
    pes.append(int(input("Digite a idade de uma pessoa: ")))
    regis.append(pes[:])
    pes.clear()
for p in range(0,len(regis)):
    print(f"{"[":=>20}Registro:{p}{"]":=<20}")
    print(f"-Nome: {regis[p][0]}\n-Idade: {regis[p][1]}")
    if regis[p][1]<18:
        mem[0]+=1
    elif regis[p][1]>=18:
        mem[1]+=1
print(f"Há {mem[0]} menores de idade\nHá {mem[1]} maiores de idade")