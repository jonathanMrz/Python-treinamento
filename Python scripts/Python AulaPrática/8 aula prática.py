for c in range(0,6,2):
    print(c)
print("Fim")

n=int(input("Digite a quantidade de vezes que o loop ira rodar: "))
for d in range(0,n+1):
    if d%2==0:
        print("{} - Loop Par".format(d))
    else:
        print("{} - Loop Impar".format(d))