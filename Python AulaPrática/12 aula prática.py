#Variaveis
us=[]
regis=[]
#Código
print("=-"*20)
regis=[input("Nome completo: ").strip().title(),
                int(input("Idade: ")),
                input("[F/M]Sexo: ").strip().upper()[0],
                input("CPF: ").strip(),
                input("Número de telefone: "),
                input("E-mail: ")]
print("Deseja mudar algum dos dados registrados? ")
print("=-"*20)
us[0]=input("[Sim/Não]: ").strip().upper()[0]
print("=-"*20)
while us[0] in "S":
    print(f"Nome: {regis[0]}\nIdade: {regis[1]}\nSexo: {regis[2]}\nCPF: {regis[3]}\nNúmero de telefone: {regis[4]}\nE-mail: {regis[5]}")
    print("=-"*20)
    us[1]=input("Digite oque deseja alterar: ").strip()
    print("=-"*20)