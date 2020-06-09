#Secuencias collatz


N = 436 #estos son los ultimos 3 digitos de mi carnet, 201612436
#N=6

def collatz(numero_collatz):#este metodo calcula la secuencia de collantz del numero a evaluar
    lista_collantz.append(numero_collatz)
    while numero_collatz>1:#while que revisa si el numero ha llegado a 1
        if numero_collatz%2==0:#si el numero es par hace N/2
            numero_collatz=numero_collatz//2
            lista_collantz.append(numero_collatz)
        else:#si es impar hace la funcion 3N+1
            numero_collatz=3*numero_collatz+1
            lista_collantz.append(numero_collatz)

    return lista_collantz

def Agregar_a_texto(lista_collantz,file="/home/abraham/Documentos/201612436-Cortos980/corto1/collatz.txt"):#este metodo agrega las listas de las secuencias al archivo de texto
    archivo = open(file,"a")#abre el archivo
    archivo.write("\n")#de aqui en adelante escribe en el archivo de texto.
    archivo.write("[")
    for i in lista_collantz:
        lista_aux=str(i)
        archivo.write(lista_aux)
        archivo.write(",")
    archivo.write("]")
    archivo.close()

#esta parte es para refresacar el documento en dado caso se corra de nuevo el programa, esta parte escribe en el documento algo vacio.
archivo1=open("/home/abraham/Documentos/201612436-Cortos980/corto1/collatz.txt","w")
archivo1.write("")
archivo1.close()
#

for i in range(2,N+1):
    lista_collantz=[]#lista que guardara los elementos de la secuencia de Collantz
    lista_collantz=collatz(i)
    Agregar_a_texto(lista_collantz)
    print(lista_collantz)
