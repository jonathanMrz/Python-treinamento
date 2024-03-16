prod=[]
val=[]
cnt=["S",0,0,0]
while True:
    prod.append(input("Nome do produto: ").strip().lower())
    while prod.count(prod[cnt[1]])>1:
        print("-="*20);print("Produto repetido!")
        prod[cnt[1]]=input("Nome do produto: ").strip().lower()
    while True:
        try:
            val.insert(cnt[1],float(input("Preço do produto: ")))
            break
        except:
            print("-="*20);print("Digite um valor válido!")
    print("-="*20)
    cnt[1]+=1
    cnt[0]=input("Deseja adicionar mais um produto?\n[S/N]: ")[0].strip().upper()
    while cnt[0] not in "SN":
        print("-="*20);print("Digite um valor válido!")
        cnt[0]=input("Deseja adicionar mais um produto?\n[S/N]: ")[0].strip().upper()
    print("-="*20)
    if cnt[0] in "N":
        break
for cnt[1] in range(0,len(prod)):
    print(f"[{cnt[1]}]{prod[cnt[1]]:.<20} {val[cnt[1]]}")
cnt[0]=input("Deseja alterar algum dos valores?\n[S/N]: ")[0].strip().upper()
print("-="*20)
while True:
    while True:
        try:
            cnt[2]=int(input("Digite o número que corresponde ao produto que desja alterar: "))
            break
        except:
            print("Tente denovo")
    print("-="*20);print(f"{cnt[2]}-{prod[cnt[2]]:.<20} {val[cnt[2]]}");print("-="*20)
    cnt[3]=input("Oque quer fazer?:\n[0]Apagar\n[1]Mudar o nome\n[2]Mudar o preço\n[3]Sair\n").strip()
    print("-="*20)
    if cnt[3] in "0":
        del(prod[cnt[2]]);del(val[cnt[2]])
        print("Produto deleteado com sucesso")
    elif cnt[3] in "1":
        prod[cnt[2]]=input("Qual será o novo nome do produto? ").strip().lower()
        while prod.count(prod[cnt[2]])>1:
            print("-="*20);print("Produto repetido!")
            prod[cnt[1]]=input("Nome do produto: ").strip().lower()
        print("Nome do produto alterado com sucesso")
    elif cnt[3] in "2":
        while True:
            try:
                val[cnt[2]]=float(input("Qual será o novo valor do produto? "))
                break
            except:
                print("-="*20);print("Digite um valor válido!")
    elif cnt[3] in "3":
        print()
    else:
        print("Digite um valor válido!")
    print("-="*20)
    for cnt[1] in range(0,len(prod)):
        print(f"[{cnt[1]}]{prod[cnt[1]]:.<20} {val[cnt[1]]}")
    print("-="*20)
    cnt[0]=input("Deseja alterar mais algum dos valores?\n[S/N]: ")[0].strip().upper()
    while cnt[0] not in "SN":
        print("Digite um valor válido!")
        cnt[0]=input("Deseja alterar mais algum dos valores?\n[S/N]: ")[0].strip().upper()
    if cnt[0] in "N":
        break