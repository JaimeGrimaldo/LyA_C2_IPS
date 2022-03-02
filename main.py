from distutils import command
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
boton = Button(ventana, text = "Validar", font =("Roboto 20"), width =13, height =1, command = lambda:evaluar())
boton.grid(row = 1, column = 0)
ventana.mainloop()