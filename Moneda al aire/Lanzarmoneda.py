import random
import time
opc="si"
while opc == "si"or opc== "s":

    print("Lanzaré una moneda 100 veces. adivina cuantas veces caerá Cara.")
    input("Presiona enter para continuar... ")
    lanzamiento=0
    cara=0
    while lanzamiento <100:
        if random.randint(0,1) == 1:
            cara=cara+1
        lanzamiento=lanzamiento+1
        if lanzamiento == int(90):
            time.sleep(2)
            print ("900 y hubo "+ str(cara)+ " Caras.")
        if lanzamiento==int(50):
            time.sleep(2)
            print ("50 y hubo "+ str(cara)+ " Caras.")
        if lanzamiento == int(10):
            time.sleep(2)
            print ("10, hay " +str(cara)+" Caras.")
    print("Cuantas caras tocaron?")
    num=input()
    time.sleep(1)
    print ("hubo "+str(cara)+" Caras")
    if str(cara) == num:
        print("Acertaste!!")
    else:
        print("Mala Suerte")
    print('Queres jugar denuevo?... Ingresa "si" o "s"')
    opc = input()
