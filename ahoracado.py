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

#se crea la funcion para mostrar el espacio de palabras.
def espacios(my_dict,palabra):
    if len(my_dict)==0:
        print('_ '*len(palabra))


#-------- aqui se se define la función principal del juego-------------------------------
def run():

 #primero se limpa la consola.
    os.system('cls')

 #se lee el archivo data.txt, se arroja la palabra aleatorioa y se asigna a una variable
    palabra =archivo_read()
    print (palabra)

#vamos a colocar la palabra dentro de una lista
    my_list = [i for i in palabra]
   
#vamos a crear una nueva lista que enumere los caracterteres de la palabra
    lista_final = list(enumerate(my_list))

#vamos a entrar en un ciclo para que el usuario verifique la palabra.
    my_dict={}
    contador = 0
    
    while contador != len(palabra):

        letra = input('ingrese una letra: ')

 # se va a colocar una afirmacion tipo assert preguntando si es string(true), o numero(false)
        assert not letra.isnumeric(),'solo se pueden ingresar letras, no números'

 #se va a hacer un diccionario, donde en caso de que se acierte la letra, se guarde en la llave la posicion y en el valor la letra.  
        for i, j in lista_final:
            if letra==j:
                my_dict[i]=j
                contador =contador+1

        print (my_dict)
        print (len(my_dict))

 # se crea una interfaz donde se muestra la posicion de las palabras acertadas
        for i in range(len(palabra)):
            if bool(my_dict.get(i))==True:
                print(my_dict.get(i), end= " ")
            else:
                print ('_', end=" ")
        
        print('\n')
    
    
        

if __name__ =='__main__':
    run()