#se importan los modulos que se van a usar
import os
import random

#funcion para leer el archivo y sacar palabra aleaotoria.
def archivo_read():
    with open('./data.txt', 'r', encoding ='utf-8') as f:
        lista_palabras = []
        for i in f.read().split('\n'):
            i.strip()
            lista_palabras.append(i)
    f.close()
    random_word = random.choice(lista_palabras)
    return random_word


def run():
    #primero se limpa la consola.
    os.system('cls')

    #se lee el archivo data.txt, se arroja la palabra aleatorioa y se asigna a una variable
    palabra =archivo_read()
    print (palabra)

    #vamos a colocar la palabra dentro de un diccionaro
    my_dict = {i: palabra[i] for i in range(len(palabra))}
    print(my_dict)
   
   #vamos a entrar en un ciclo para que el usuario verifique la palabra.

    contador = 0
    while contador != len(palabra):

        letra = input('ingrese una letra: ')

        # se va a colocar una afirmacion tipo assert preguntando si es string(true), o numero(false)
        assert not letra.isnumeric(),'solo se pueden ingresar letras, no números'

        #se va a hacer una lista oculta para guardar las posiciones de la letra
        lista_oculta =[]
        for i in range(len(palabra)):
            if letra == palabra[i]:
                lista_oculta.append(i)
                contador = contador +1

        print(lista_oculta)


        
        

if __name__ =='__main__':
    run()