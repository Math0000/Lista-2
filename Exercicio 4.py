'''
Esse programa escreve os números por extenso
Aluno: Matheus Moreira do Nascimento
DRE: 119042060
Curso: Matemática Aplicada
Disciplina: Topicos da Matemática Aplicada A
'''

print("...................................................................... \n")
print("Essa parada aqui escreve o nome por extenso de qualquer número")
print("positivo menor que 100000 ")
print('Testa aí po, escreve qualquer número positivo menor que 100000 \n')
print("...................................................................... \n")


Dici1 = {

  0:'zero',

  1:'um',

  2:'dois',

  3:'três', 

  4:'quatro',

  5:'cinco',

  6:'seis', 

  7:'sete',

  8:'oito', 

  9:'nove'}


Dici2 = {

  11:'onze',

  12:'doze',

  13:'treze',

  14:'quatorze',

  15:'quinze',

  16:'dezesseis' , 

  17:'dezessete',

  18:'dezoito',

  19:'desenove'}


Dici3 = {

  10:'dez',

  20:'vinte',

  30:'trinta',

  40:'quarenta',

  50:'cinquenta',

  60:'sessenta',

  70:'setenta',

  80:'oitenta',

  90:'noventa'}


Dici4 = {

  2:'vinte e ',

  3:'trinta e ',

  4:'quarenta e ',

  5:'cinquenta e ',

  6:'sessenta e ',

  7:'setenta e ',

  8:'oitenta e ',

  9:'noventa e '}


Dici5= {

  0:'',

  1:'cento e ',

  2:'duzentos e ',

  3:'trezentos e ', 

  4:'quatrocentos e ',

  5:'quinhentos e ',

  6:'seiscentos e ', 

  7:'setecentos e ',

  8:'oitocentos e ',

  9:'novecentos e '}


Dici6 = {

  100:'cem',

  200:'duzentos',

  300:'trezentos', 

  400:'quatrocentos',

  500:'quinhentos',

  600:'seiscentos', 

  700:'setecentos',

  800:'oitocentos',

  900:'novecentos'}


def dezenas(x):

    if x < 10:

        extenso = Dici1[x]

        

    elif x > 10 and x < 20:

        extenso = Dici2[x]


    elif x%10==0:

        extenso = Dici3[x]


    else:

        resto = x%10

        dezena = (x - resto)/10

        extenso = Dici4[dezena] + Dici1[resto]

    return (extenso)




def cent(x):


    if x%100==0:

        extenso = Dici6[x]


    else:

        resto= x%100

        centena = (x-resto)/100

        extenso = Dici5[centena] + dezenas(resto)

    return (extenso)



def mil(x):

    if x==1000:

       print("mil")


    elif x%1000==0:

        num=x/1000

        extenso = dezenas(num)+str(" mil")


    elif x > 1000 and x<2000:

        resto= x%1000

        if resto%100==0 or resto<100:

            extenso = str(" mil e ") + cent(resto)


        else:

            extenso = str(" mil ") + cent(resto)


    else:

        resto= x%1000

        if resto%100==0 or resto<100:

            num = (x-resto)/1000

            extenso = dezenas(num) + str(" mil e ") + cent(resto)


        else:

            num = (x-resto)/1000

            extenso = dezenas(num) + str(" mil ") + cent(resto)

       

    return (extenso)



while True:
    x = int(input("Escreve aí o número que tu quer por extenso "))
    print("")
    if x<100:

        print("~"*70)
        print("Esse número aí é o",dezenas(x))
        print("~"*70)
        print("")
        
        print("Se tu quiser ver outro número digita 'sim',")
        z=str(input("se não quiser, digita 'não' "))
        if z!=str('sim'):
            break
        print("")
    
    elif x > 99 and x < 1000:

        print("~"*70)
        print("Esse número aí é o",cent(x))
        print("~"*70)
        print("")
        
        print("Se tu quiser ver outro número digita 'sim',")
        z=str(input("se não quiser, digita 'não' "))
        if z!=str('sim'):
            break
        print("")

    elif x > 999 and x < 100000:

        print("~"*70)
        print("Esse número aí é o",mil(x))
        print("~"*70)
        print("")
        
        print("Se tu quiser ver outro número digita 'sim',")
        z=str(input("se não quiser, digita 'não' "))
        if z!=str('sim'):
            break
        print("")
    
    else:

        print("Esse numero aí é muito grande brother")
        print("Nem tá no banco de dados po, o bagulho")
        print("só lê mundo menor que 100000")
        print("")
        
        print("Se tu quiser ver outro número digita 'sim',")
        z=str(input("se não quiser, digita 'não' "))
        if z!=str('sim'):
            break
        print("")
    
print("")
print("Suave")
print("É nós")
