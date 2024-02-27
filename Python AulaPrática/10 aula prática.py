n=0
s=0
while True:
    n=int(input("[999=stop]Digite um número: "))
    if n==999:
        break
    s+=n
print(f"A soma dos números digitados é igual a {s}")