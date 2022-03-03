from distutils import command
from re import I
from tkinter import *
import webbrowser

'''''
 EJEMPLOS DE IPv4
    Clase A: 10.0.0.0 a 10.255.255.255
    Clase B: 172.16.0.0 a 172.31.255.255
    Clase C: 192.168.0.0 a 192.168.255.255

    La clase A comienza con 10, despues sus demas numeros son del 0 al 255
    La clase B comienza con 172, despues su siguiente numero va del 16 a 31 y de ahi puro 0 a 255
    La clase C comienza con 192, despues 168 y de ahi 0 a 255
'''''

ventana = Tk()
ventana.title("Validación de Ip's")
#ventana.geometry("500x200")
#Entrada

flag2 = False
flag3 = False
flag4 = False

def reiniciarFlags():
    flag2 = False
    flag3 = False
    flag4 = False


def abrirA():
    path = 'TipoA.html'
    webbrowser.open_new(path)

def abrirB():
    path = 'TipoB.html'
    webbrowser.open_new(path)

def abrirC():
    path = 'TipoC.html'
    webbrowser.open_new(path)


def claseA(seccion2, seccion3, seccion4):
    global flag2, flag3, flag4
    print("Aca tenemos las secciones:",seccion2,seccion3,seccion4)

    print("Sumar a + b:",seccion2 + seccion3)

    for i in range(256):
        if seccion2 == i:
            print("Encontrado:",i)
            flag2 = True
            break
    for i in range(256):
        if seccion3 == i:
            print("Encontrado:",i)
            flag3 = True
            break
    for i in range(256):
        if seccion4 == i:
            print("Encontrado:",i)
            flag4 = True
            break
    if flag2 == True and flag3 == True and flag4 == True:
        print("Dirección IPv4 válida.")
        print("Clase A")
        abrirA()
    else:
        print("---ERROR: Direccion IPv4 invalida.")
    reiniciarFlags()
    
def claseB(seccion2, seccion3, seccion4):
    global flag2, flag3, flag4
    for i in range(32):
        if i >= 16:
            if seccion2 == i:
                flag2 = True
                break
        if i < 16:
            flag2 = False
    for i in range(256):
        if seccion3 == i:
            print("Encontrado:",i)
            flag3 = True
            break
    for i in range(256):
        if seccion4 == i:
            print("Encontrado:",i)
            flag4 = True
            break
    if flag2 == True and flag3 == True and flag4 == True:
        print("Dirección IPv4 válida.")
        print("Clase B")
    else:
        print("---ERROR: Direccion IPv4 invalida.")
    reiniciarFlags()
    abrirB()

def claseC(seccion2, seccion3, seccion4):
    global flag2, flag3, flag4
    if seccion2 == 168:
        #print("Entra flag2 verdadero")
        flag2 = True
    else:
        flag2 = False
    for i in range(256):
        if seccion3 == i:
            print("Encontrado:",i)
            flag3 = True
            break
    for i in range(256):
        if seccion4 == i:
            print("Encontrado:",i)
            flag4 = True
            break
    if flag2 == True and flag3 == True and flag4 == True:
        print("Dirección IPv4 válida.")
        print("Clase C")
    else:
        print("---ERROR: Direccion IPv4 invalida.")
    
    reiniciarFlags()
    abrirC()
    
banderaPuntos = False

def evaluar_puntos_IP():
    global banderaPuntos
    ip = field.get()
    contadorPuntos = 0
    for i in range(len(ip)):
        if ip[i] == ".":
            contadorPuntos = contadorPuntos + 1
    if contadorPuntos == 3:
        print("Puntos validados")
        banderaPuntos = True
    else:
        print("ERROR: Hay un problema con la contabilidad de los puntos")


def ciclos(seccion1, seccion2, seccion3, seccion4):
    valor = ""
    validarParte1 = False
    validarParte1_2 = False
    validarParte1_3 = False
    indice = 0
    ip = field.get()
    ip_split = ip.split(".")
    parte1 = ip_split[0]
    parte2 = ip_split[1]
    parte3 = ip_split[2]
    parte4 = ip_split[3]
    print(ip_split)
    while indice < 10:
        if int(parte1[0]) == indice:
            print("1 Encontrado:",indice)
            valor = valor + str(indice)
            validarParte1 = True
        if int(parte1[1]) == indice:
            print("2 Encontrado:",indice)
            valor = valor + str(indice)
            validarParte1_2 = True
        if len(parte1) == 3:
            if int(parte1[2]) == indice:
                print("3 Encontrado:",indice)
                valor = valor + str(indice)
                validarParte1_3 = True
        indice = indice + 1
    print("Numeros encontrados de parte 1:",valor)
    if validarParte1 == True and validarParte1_2 == True and validarParte1_3 == True:
        print("Valor reacomodado:",parte1)
    else:
        if validarParte1 == True and validarParte1_2:
            print("Valor reacomodado:",parte1,type(int(parte1)))
    
    if parte1 == "10" or int(parte1) != 192 or int(parte1) != 172:
        print("ERROR: Clase no identificada")
        if int(parte1) == 10:
            print("Clase A")
    else:
        if int(parte1) == 172:
            print("Clase B")
        if int(parte1) == 192:
            print("Clase C")
    
    

def evaluarOperadoresRE(re_spliteado):
    global banderaPuntos
    bandera1 = False
    bandera2 = False
    bandera3 = False
    bandera4 = False

    seccion1 = re_spliteado[0]
    seccion2 = re_spliteado[2]
    seccion3 = re_spliteado[4]
    seccion4 = re_spliteado[6]

    for i in range(len(seccion1)):
        if seccion1[i] == "+":
            #print("+ Encontrado seccion 1")
            bandera1 = True
            break
    for i in range(len(seccion2)):
        if seccion2[i] == "+":
            #print("+ Encontrado seccion 2")
            bandera2 = True
            break
    for i in range(len(seccion3)):
        if seccion3[i] == "+":
            #print("+ Encontrado seccion 3")
            bandera3 = True
            break
    for i in range(len(seccion4)):
        if seccion4[i] == "+":
            #print("+ Encontrado seccion 4")
            bandera4 = True
            break
    if bandera1 == True and bandera2 == True and bandera3 == True and bandera4 == True:
        evaluar_puntos_IP()
        if banderaPuntos == True:
            if field.get() != "":
                ciclos(seccion1, seccion2, seccion3, seccion4)
            else:
                print("Error, field vacio")


def RE():
    expresion_regular = "(0…9)+ (.) (0…9)+ (.) (0…9)+ (.) (0…9)+"
    expresion_regular = expresion_regular.replace("(","").replace(")","").replace("…","_")
    split_er = expresion_regular.split(".")
    split_er_String =  "".join(split_er)
    split_er_String = split_er_String.split(" ")
    print("Esto tiene SPLIT:",expresion_regular,"\n",split_er_String)
    evaluarOperadoresRE(split_er_String)
    


def evaluar():
    ip = field.get()
    contadorPuntos = 0

    for i in range(len(ip)):
        if ip[i] == ".":
            contadorPuntos = contadorPuntos + 1

    if contadorPuntos == 3:
        print("---Esto contiene el field:",ip)
        ipSplit = ip.split(".")
        print("---Spliteado:",ipSplit)
        seccion1 = int(ipSplit[0])
        seccion2 = int(ipSplit[1])
        seccion3 = int(ipSplit[2])
        seccion4 = int(ipSplit[3])

        if seccion1 == 10:
            print("Entra a clase A")
            claseA(seccion2, seccion3, seccion4)
        if seccion1 == 172:
            print("Entra a clase B")
            claseB(seccion2, seccion3, seccion4)
        if seccion1 == 192:
            print("Entra a clase C")
            claseC(seccion2, seccion3, seccion4)
        print("\n")
    else:
        print("Hay un problema con la IP")
        


    


field = Entry(ventana,font =("Roboto 20"))
field.grid(row = 0, column = 0, padx = 50, pady = 30, columnspan =1)
boton = Button(ventana, text = "VALIDAR", font =("Roboto 20"), width =13, height =1, command = lambda:evaluar())
boton.grid(row = 1, column = 0)
ventana.mainloop()