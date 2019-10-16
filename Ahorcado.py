import random
import os

palabras=["abeja", "beso","casa","dedo","elfo",
"frasco","gente","hijo","iguana"]

palabra=random.choice(palabras)

fallo0= '''
            !===N
                N
                N
                N
'''
fallo1='''
           !===N
           O   N
               N
               N
'''

fallo2='''
           !===N
           O   N
          -    N
               N
'''
fallo3='''
           !===N
           O   N
          - -  N
               N
'''

fallo4='''
           !===N
           O   N
          -I-  N
               N
'''
fallo5='''
           !===N
           O   N
          -I-  N
            \  N
'''

fallo6='''
           !===N
           O   N
          -I-  N
          /\   N
'''

letras_correctas=""
letras_todas=""
fallos=0

while True:
    os.system("cls")
    print("------------------")
    print("++++++++Juego del ahorcado+++++++")
    print("------------------")
    if fallos==0:
        print(fallo0)
    elif fallos==1:
        print(fallo1)
    elif fallos==2:
        print(fallo2)
    elif fallos==3:
        print(fallo3)
    elif fallos==4:
        print(fallo4)
    elif fallos==5:
        print(fallo5)
    elif fallos==6:
        print(fallo6)

resultado=""
for letra in palabra:
    if letra in letras_correctas:
        resultado+=letra
    else:
        resultado+="_"
print("     {}".format(resultado))
print()
print()

if resultado==palabra:
    print("Has ganado")
    #break


if fallos>5:
    print("La palabra era:" , palabra)
    print("Has perdido")
    #break

while True:
    letra_usuario_sin_formato=input("Digite una letra: ")
    letra_usuario=letra.usuario_sin_formato.upper()
    if len(letra.usuario)<1 or len(letra.usuario)>1:
        print("Introduce una letra")
    elif letra.usuario in letra_todas:
        print("Esa letra ya la has dicho")
    elif not letra_usuario.isalpha():
        print("Introduce una letra")
    else:
        letras_todas+=letra_usuario
        break

if letra_usuario not in palabra:
    fallos+=1
else:
    letras_correctas+=letra_usuario


