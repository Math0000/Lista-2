'''
Esse programa é uma calculadora vetorial simples
Aluno: Matheus Moreira do Nascimento
DRE: 119042060
Curso: Matemática Aplicada
Disciplina: Topicos da Matemática Aplicada A
'''

print("...................................................................... \n")
print("Essa bagulho aqui é uma calculado vetorial simples que trabalha")
print("somente com soma e subtração de 2 vetores no enesimo plano R ")
print('Para iniciar, digite "calc()" sem as aspas \n')
print("...................................................................... \n")

def soma():

    U=[]
    V=[]

    a=int(input("Os seus vetores tão em que plano? "))
    print("suave \n")
    
    for i in range(1,a+1):
          i=float(input("Qual a coordenada do primeiro vetor u no R" +str(i)+" "))
          U .append(i)
    print("")
    print("u =", U)
    print("Fecho \n")

    for i in range(1,a+1):
          i=float(input("Qual a coordenada do segundo vetor v no R" +str(i)+" "))
          V .append(i)
    print("")
    print("v =", V)
    print("Fecho \n")

    D=[]
    D=[elemU + elemV for elemU, elemV in zip(U, V)]

    print("A soma dos seus vetores é igual a w =", D)
    print("")
    print("Fim da operação")
    print("")
    calc()

def subtração():

    U=[]
    V=[]

    a=int(input("Os seus vetores tão em que plano? "))
    print("suave \n")
    
    for i in range(1,a+1):
          i=float(input("Qual a coordenada do primeiro vetor u no R" +str(i)+" "))
          U .append(i)
    print("")
    print("u =", U)
    print("Fecho \n")

    for i in range(1,a+1):
          i=float(input("Qual a coordenada do segundo vetor v no R" +str(i)+" "))
          V .append(i)
    print("")
    print("v =", V)
    print("Fecho \n")

    D=[]
    D=[elemU - elemV for elemU, elemV in zip(U, V)]

    print("A subtração dos seus vetores é igual a w =", D)
    print("")
    print("Fim da operação")
    print("")
    calc()
    

def opção():

    print("~"*25)
    print("1) Soma de Vetores\n")
    print("2) Subtração de Vetores\n")
    print("3) Sair da Calculadora")
    print("~"*25)
    oper=int(input("Qual opção você quer? "))
    if oper==1:
        print("Suave\n")
        soma()        
                
    elif oper==2:
        print("Suave\n")
        subtração()        
        
    elif oper==3:
        print("Suave")
        print("É nós")
        
    else:
        print("")
        print("Essa opção nem ta no programa brother")
        print("Tenta de novo ai")
        opção()
    return
    
    return
def calc():
    
    print("               Bem vindo a calculado vetorial              ")
    print("Digita ai o numero da operação com qual você quer trabalhar\n")
    opção()
    return
    
   
