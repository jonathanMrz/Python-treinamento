import random as rd
#Primeira questão[===============================================================]
n0=s0=loops0=0
while True:
    print("[999=Stop]")
    n0=int(input("Digite um número: "))
    if n0==999:
        print("Fim do programa")
        break
    s0+=n0; loops0+=1
print(f"Soma dos valores digitados: {s0}\nQuantidade de loops: {loops0}")
#Segunda questão[================================================================]
nt0=0
while True:
    print("[Valor negativo ira para o programa]")
    nt0=int(input("Você quer ver a tabuada de qual valor? "))
    if nt0<0:
        print("Fim do programa")
        break
    print("-"*15,f"Tabuada de {nt0}","-"*15)
    print(f"""{nt0}x1={nt0*1}\n{nt0}x2={nt0*2}\n{nt0}x3={nt0*3}\n{nt0}x4={nt0*4}\n{nt0}x5={nt0*5}
{nt0}x6={nt0*6}\n{nt0}x7={nt0*7}\n{nt0}x8={nt0*8}\n{nt0}x9={nt0*9}\n{nt0}x10={nt0*10}""")
    print("-"*42)
#Terceira questão[===============================================================]
player0=0
pc0=rd.randint(1,10)
iorp=""
qdv=0
while True:
    iorp=input("[I/P]Impar ou Par: ").strip()
    player0=int(input("Escolha um valor: "))
    print("🏁"*20)
    if iorp in "Ii" and (player0+pc0)%2==0:
        print(f"""O player escolheu impar e jogou: {player0}\nO computador escolheu par e jogou: {pc0}
Deu Par: {player0+pc0}\nFim de jogo!""")
        print("🏁"*20)
        break
    elif iorp in "Pp" and (player0+pc0)%2!=0:
        print(f"""O player escolheu par e jogou: {player0}\nO computador escolheu impar e jogou: {pc0}
Deu Impar: {player0+pc0}\nFim de jogo!""")
        print("🏁"*20)
        break
    elif iorp in "Ii" and (player0+pc0)%2!=0:
        print(f"""O player escolheu impar e jogou: {player0}\nO computador escolheu par e jogou: {pc0}
Deu impar: {player0+pc0}\nVocê ganhou!""")
        print("🏁"*20)
    elif iorp in "Pp" and (player0+pc0)%2==0:
        print(f"""O player escolheu par e jogou: {player0}\nO computador escolheu impar e jogou: {pc0}
Deu par: {player0+pc0}\nVocê ganhou!""")
        print("🏁"*20)
    qdv+=1
print(f"Pontuação de vítoria: {qdv*100}")
#Quarta questão[=================================================================]
sex0=cnt=""
idade0=mdi=hms=mmqv=0
while True:
    print("="*10,"| Cadastro |","="*10)
    idade0=int(input("Digite sua idade: "))
    sex0=input("[M/F]Digite seu sexo: ").strip()
    while sex0 not in "FfMm":
        print("Valor invalido.")
        sex0=input("[M/F]Digite seu sexo: ").strip()
    if idade0>18:
        mdi+=1
    elif sex0 in "Mm":
        hms+=1
    elif sex0 in "Ff" and idade0<20:
        mmqv+=1
    print("-"*20)
    cnt=input("[S/N]Quer continuar? ")
    while cnt not in "NnSs":
        print("Digit um valor válido")
        cnt=input("[S/N]Quer continuar? ")
        if cnt in "Nn":
            break
    if cnt in "Nn":
        break
print("-"*20)
print(f"Maiores de idade: {mdi}\nHomens cadastrados: {hms}\nMulheres com menos de 20 anos: {mmqv}")
print("="*10,"| Fim do Programa |","="*10)
#Quinta questão[=================================================================]
nm0=cnt0=pmc=""
preco0=soma=mqm=pdmc=0
while True:
    nm0=str(input("Escreva o nome do produto: "))
    preco0=int(input("Informe o preço do produto: "))
    if preco0>1000:
        mqm+=1
    if soma==0 or preco0 > pdmc:
        pmc=nm0
        pdmc=preco0
    soma+=preco0
    cnt0=str(input("[S/N]Quer adicionar mais um produto? ")).strip()
    while cnt0 not in "SsNn":
        print("Digite uma resposta valida.")
        cnt0=str(input("[S/N]Quer adicionar mais um produto? ")).strip()
        if cnt0 in "Nn":
            break
    if cnt0 in "Nn":
        break
print(f"A soma de todos produtos: {soma}\nQuantidade de produtos com o preço acima de 1000: {mqm}\nProduto mais caro: {pmc}")