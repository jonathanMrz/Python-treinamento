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
list_main=[]
list_par=[]
list_imp=[]
for lp in range(1,8):
    while True:
        try:
            list_main.append(int(input(f"Ensira o {lp}º valor: ")))
            break
        except:
            print("DIgite um valor válido!\n","-="*20)
for sp in range(0,len(list_main)):
    if list_main[sp]%2==0:
        list_par.append(list_main[sp])
    elif list_main[sp]%2!=0:
        list_imp.append(list_main[sp])
print(f"""Lista dos números digitados: {sorted(list_main)}\nLista dos números pares: {sorted(list_par)}
Lista dos números impares: {sorted(list_imp)}""")
#Terceira e Quarta questão[======================================================]
list_l0=[]
list_l1=[]
list_l2=[]
sol=[0,0,0]

for c in range(0,3):
    list_l0.append(int(input(f"Digite o número da posição {c}x0: ")))
for c in range(0,3):
    list_l1.append(int(input(f"Digite o número da posição {c}x1: ")))
for c in range(0,3):
    list_l2.append(int(input(f"Digite o número da posição {c}x2: ")))
print(f'{list_l0}\n{list_l1}\n{list_l2}')

for c in range(0,len(list_l0)):
    if list_l0[c]%2==0:
        sol[0]+=list_l0[c]
    if list_l1[c]%2==0:
        sol[0]+=list_l1[c]
    if list_l2[c]%2==0:
        sol[0]+=list_l2[c]
print(f'A soma de todos os valores pares: {sol[0]}')

sol[1]= list_l0[2]+list_l1[2]+list_l2[2]
print(f"A soma de todos os valores da terceira coluna: {sol[1]}")

sol[2]= max(list_l1)
print(f"O maior valor da segunda linha: {sol[2]}")
#Quinta questão[=================================================================]
import random as rd
import time as tm
print("--"*20,f"\n{"MEGA CENA": >20}\n","--"*20)
qnts=int(input("Você deseja rodar quantos números da Mega Cena? "))
for c in range(1,qnts+1):
    tm.sleep(1)
    val=[rd.randrange(0,60),rd.randrange(0,60),rd.randrange(0,60),rd.randrange(0,60),rd.randrange(0,60),rd.randrange(0,60)]
    print(f"Jogada {c}º :{val}")
#Sexta questão[==================================================================]
list_regis=[]
list_alu=[]
nota=[]
cnt=0
while True:
    list_alu.append(input("Digite o nome de um aluno: ").strip().title())
    while True:
        try:
            nota.append(float(input("Digite sua primeira nota: ")))
            nota.append(float(input("Digite sua segunda nota: ")))
            break
        except:
            print("Digite um valor válido!")
    list_alu.append(nota[:])
    list_regis.append(list_alu[:])
    list_alu.clear();nota.clear()
    cnt=input("[S/N]Deseja adicionar mais um aluno? ").upper().strip()
    while cnt[0] not in "SN" or cnt in "":
        print("Digite um valor valido!")
        cnt=input("[S/N]Deseja adicionar mais um aluno? ").upper().strip()
    if cnt[0] in "N":
        break
print("=="*20,f"\n{"Nº": <10}{"Nome": <25}{"MÉDIA"}");print("=="*20)
for c in range(0,len(list_regis)):
    print(f"{c: <8}  {list_regis[c][0]: <20}     {(list_regis[c][1][0]+list_regis[c][1][1])/2:.2f}")
while c!=999:
    c=int(input("[999 interrompe]Digite o número do aluno para ver sua nota: "))
    print("=="*20)
    try:
        print(f"Primeira nota: {list_regis[c][1][0]: <5} Segunda nota: {list_regis[c][1][1]}")
    except:
        print("Fim do programa.")
    print("=="*20)