import os

#funcion para leer el archivo
def archivo_read():
    with open('./data.txt', 'r', encoding ='utf-8') as f:
        lista_palabras = []
        for i in f.read().split('\n'):
            i.strip()
            lista_palabras.append(i)
    f.close()
    return lista_palabras


def run():
    #primero se limpa la consola.
    os.system('cls')
    print(archivo_read())




if __name__ =='__main__':
    run()