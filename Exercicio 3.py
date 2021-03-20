'''
Esse programa calcula o maior primo do numero 3852914583882
Aluno: Matheus Moreira do Nascimento
DRE: 119042060
Curso: Matemática Aplicada
Disciplina: Topicos da Matemática Aplicada A
'''
print("................................................................................\n")
print("Essa parada aqui calcula o maior fator primo do numero 3852914583882")
print('Pra obter o calculo digita "ver"')
print("................................................................................\n")

a=input("Digita ai")
if a==str('ver'):
    b=3852914583882
    e=2
    while b>1:
        if b%e==0:
            b=b/e
        else:
            while b%e!=0:
                e+=1

    print("O maior primo de",3852914583882," é :")
    print("..")
    print(e)
    print("..")
