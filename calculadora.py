#crear funciones para las operaciones

import os


def sumar(n1, n2):
    return n1 + n2

def restar (n1, n2):
    return n1 - n2

def multiplicar (n1, n2):
    return n1, n2

def dividir (n1,n2):
    try: 
        return n1/n2
    except: 
        print(" no se puede dividir por cero ")



#funcion con menu

def menu():
    os.system("cls") #para limpiar la consola
    print("+ para sumar")
    print("- para restar")
    print("* para multiplicar")
    print("/ para dividir")
    print ("s para salir")

#funcion principal

def main():
    menu()
    op=input("Ingrese una operación ")
    while op != "s":
        pn= int (input("Ingrese un numero: "))
        sn= int (input("Ingrese otro numero: "))
        if(op=="+"):
            print("El resultado de la suma es: " , sumar (pn,sn))
        elif(op=="-"):
            print("El resultado de la resta es: " , restar (pn,sn))
        elif(op=="*"):
            print("El resultado de la multiplicación es: " , multiplicar (pn,sn))
        elif(op=="/"):
            print("El resultado de la división es: " , dividir (pn,sn))
        elif(op=="s"):
            print("Ha salido del programa  🙃")
        else:
            print("La opción no es válida")
        op=input("Ingrese una operacion ")
        break

#aca empieza el programa
main()






