'''
Esse programa calcula a soma dos digitos das potências de 2
Aluno: Matheus Moreira do Nascimento
DRE: 119042060
Curso: Matemática Aplicada
Disciplina: Topicos da Matemática Aplicada A
'''

print("................................................................................\n")
print("Essa parada calcula a soma dos algarismos das potências de 2")
print('Pra começar, digita qual potência de 2 você quer\n')
print("................................................................................\n")

while True:
    a=int(input("Digita ai "))

    f=2**a
    m = int(0)

    while f!=0:
        r = f%10
        f = (f-r)//10
        m = (m+r)
    
    print("A soma dos algarismos de 2 elevado a",a," é :")
    print(".............................................")
    print(m)
    print(".............................................\n")
    
    print("Se tu quiser calcular com outra potência")
    z=str(input("digita 'sim', se não quiser, digita 'não' "))
    if z!=str('sim'):
        break
    print("")
    
print("")
print("Suave")
print("É nós")
