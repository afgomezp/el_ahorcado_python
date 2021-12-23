import os

#funcion para leer el archivo
def archivo_read():
    with open('./data.txt', 'r', encoding ='utf-8') as f:
        lista_palabras = []
        for i in f.read().split('\n'):
            i.strip()
            lista_palabras.append(i)
   

    #llevar la lista de palabras a otro archivo
    with open('./listaverificacion.txt', 'w', encoding ='utf-8') as f2:
        for i in lista_palabras:
            f2.write(i)
            f2.write('$')
            f2.write('\n')
    
    f.close()
    f2.close()


    return lista_palabras

#llevar la lista de palabras a otro archivo


def run():
    #primero se limpa la consola.
    os.system('cls')
    print(archivo_read())




if __name__ =='__main__':
    run()