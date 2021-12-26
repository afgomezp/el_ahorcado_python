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

#se crea la funcion para mostrar la interfaz del juego, se muestras espacios sin adivinar y letras adivinadas.
def interfaz(my_dict,palabra):
    os.system('cls')
    print('Adivina la palabra oculta que se muestra a continuación:' + '\n')
    for i in range(len(palabra)):
        if bool(my_dict.get(i))==True:
            print(my_dict.get(i), end= " ")
        else:
            print ('_', end=" ")
        
    print('\n')

    if len(my_dict)==len(palabra):
        print('Ganaste!')


#-------- aqui se se define la función principal del juego-------------------------------
def run():

 #se lee el archivo data.txt, se arroja la palabra aleatorioa y se asigna a una variable
    palabra =archivo_read()

#vamos a colocar la palabra dentro de una lista y a enumerarla en otra lista
    my_list = [i for i in palabra]
   
    lista_final = list(enumerate(my_list))  
    
#se va a hacer un diccionario, donde en caso de que se acierte la letra, se guarde en la llave la posicion y en el valor la letra.
    my_dict= {}

#se limpia pantalla y se corre la funcion de la interfaz.
    interfaz(my_dict,palabra)


#vamos a entrar en un ciclo para que el usuario verifique la palabra.  
    contador = 0
    
    while contador != len(palabra):

        letra = input('ingrese una letra: ')

 # se va a colocar una afirmacion tipo assert preguntando si es string(true), o numero(false)

        try:
            if letra.isalpha() ==True:

 #se va llenar el diccionario previamente creado y llamado my_dict 
                for i, j in lista_final:
                    if letra==j:
                        my_dict[i]=j
                        contador =contador+1
            
    #se invoca nuevamente la funcion interfaz para que actualice la interfaz.
                    interfaz(my_dict,palabra)
            else:
                raise TypeError
        except TypeError:
            print ('no ingresaste una letra')
    

             
        
    
       

if __name__ =='__main__':
    run()