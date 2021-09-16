#Juego piola de adivinar un numero, proximamente en Steam
import random
import time
opc = "si"
while opc == "si" or opc == "s":
    IntentosRealizados = 0
    print ('Hola!! ingrese el nombre del jugador')
    nombre = input()
    numero = random.randint(1,20)
    print ('Bueno, ' +nombre+ ' estoy pensando un numero entre 1 y 20.')
    while IntentosRealizados < 6:
        print ('Intenta Adivinar')
        estimacion = int (input())
        IntentosRealizados = IntentosRealizados + 1
        time.sleep(1)
        if IntentosRealizados == 5:
            break
        if estimacion == numero:
            break
        if estimacion < numero:
            if estimacion < numero-4:
                print ('Congelado')
            else: print('frio')
        if estimacion >numero:
            if estimacion >numero+4:
                print ('Quemado.')
            else:
                print ('caliente.')
        

    if estimacion == numero:
        IntentosRealizados = str(IntentosRealizados)
        print ('Bien hecho, ' +nombre+ ' Adivinaste el numero con tan solo '+IntentosRealizados+ ' intentos!!')
    
    if estimacion != numero:
        numero = str(numero)
        print ('Sos muy malo, el numero que estaba pensando era '+numero)
    time.sleep(2)
    print('Quieres jugar denuevo?... Ingresa "si" o "s"')
    opc = input()
