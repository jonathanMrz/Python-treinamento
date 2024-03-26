#Primeira questão[===============================================================]
regi=[];pes=[];mem=[0,0];pes_ma=[];pes_me=[];usv1=[0,0]
while True:
    print(f"{"[":=>20}#Registro: {usv1[0]}{"]":=<20}")
    pes.append(input("Digite um nome: ").strip().title())
    pes.append(int(input("Digite um peso: ")))
    regi.append(pes[:])
    pes.clear()
    usv1[0]+=1
    usv1[1]=input("Deseja adicionar mais um registro? ").strip().upper()
    while usv1[1] in "" or usv1[1][0] not in "SN" :
        print("Digite um valor válido!")
        usv1[1]=input("Deseja adicionar mais um registro? ").strip().upper()
    if usv1[1][0] in "N":
        break
print("="*30)
print(f"No geral foi cadastrado {len(regi)} pessoas.")
for p in range (0,len(regi)):
    if p==0 or regi[p][1]>=mem[0]:
        mem[0]=regi[p][1]
    if p==0 or regi[p][1]<=mem[1]:
        mem[1]=regi[p][1]
for p2 in range (0,len(regi)):
    if regi[p2][1]==mem[0]:
        pes_ma.append(regi[p2][0])
    if regi[p2][1]==mem[1]:
        pes_me.append(regi[p2][0])
print(f"""Maior peso registrado {mem[0]}Kg e a(s) pessoa(s) com este peso: {pes_ma}
Menor peso registrado {mem[1]}Kg e a(s) pessoa(s) com este peso: {pes_me}""")
    #OBS: O RESULTADO DESTE EXERCÍCIO NÃO FOI NEM UM POUCO SATISFATÓRIO.
#Segunda questão[================================================================]
#Terceira questão[===============================================================]
#Quarta questão[=================================================================]
#Quinta questão[=================================================================]
#Sexta questão[==================================================================]