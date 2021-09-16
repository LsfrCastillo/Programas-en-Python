import random
import time

def introduccion():
    print ("Estas en una tierra llena de dragones. Frente a ti")
    print ("hay dos cuevas. En una de ella, el dragon es generoso y")
    print ("amigable y compartira su tesoro contigo. El otro dragon")
    print ("es codicioso y esta hambierto, y te devorara inmediatamente.")
    print ()

def elegircueva():
    cueva = ''
    while cueva != '1' and cueva !='2':
        print('¿A que cueva quieres atrar? (1 o 2)')
        cueva = input()
    return cueva

def explorarCueva(cuevaElegida):
    print('te aproximas a la cueva...')
    time.sleep(2)
    print('Un gran dragon aparece subitamente frente a ti! abre sus fauses...')
    print()
    time.sleep(2)
    cuevaAmigable = random.randint(1, 2)

    if cuevaElegida == str(cuevaAmigable):
        print('te regala su tesoro')
    else:
        print ('Te engulle de un bocado!')

jugardenuevo = 'si'
while jugardenuevo == 'si' or jugardenuevo == 's':
    introduccion()
    numerodecueva = elegircueva()
    explorarCueva(numerodecueva)
    print('Quieres jugar de nuevo? (si o no)')
    jugardenuevo = input()
