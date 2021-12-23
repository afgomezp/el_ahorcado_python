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

    #se lee el archivo data.txt y se arroja la palabra aleatorioa
    print(archivo_read())




if __name__ =='__main__':
    run()