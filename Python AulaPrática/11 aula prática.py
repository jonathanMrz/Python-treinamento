pessoa=("CPF","nome","idade","sexo")

for people1 in pessoa:
    print(people1)
for people2 in range(0,len(pessoa)):
    print(people2)
for pos, people3 in enumerate(pessoa):
    print(people3)

print(sorted(pessoa))
print(pessoa[0])