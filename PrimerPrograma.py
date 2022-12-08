import time
import webbrowser
import os

os.system("cls")
print('¡BIENVENIDO AL CONVERTIDOR DE MONEDA LOCAL DE TU PREFERENCIA :D!')
time.sleep(3.5)

print('\nOpciones')
print('1. Convertir dólares a córdobas?')
print('2. Convertir córdobas a dólares?')
x = int(input('Seleccione una de las dos opciones: '))

if x == 1: 
    dol = float(input('\nCuantos dolares quieres cambiar a cordobas?: '))
    vc = 35.52
    cam1 = dol * vc
    cam1 = str(round(cam1, 2))
    print('Tienes '+ cam1 + ' córdobas')

elif x == 2:
    cord = float(input('\nCuantos cordobas quieres cambiar a dólares?: '))
    vd = 35.52
    cam = cord / vd
    cam = str(round (cam, 2))
    print('Tienes '+ cam + ' dólares')

time.sleep(1.5)
print('¡GRACIAS POR UTILIZARME!')
time.sleep(3)
os.system("cls")
y = input('Quieres escuchar una canción antes de irte? \n')

if y == 'si':
    webbrowser.open(url='https://www.youtube.com/watch?v=6riDJMI-Y8U&ab_channel=CrunchyrollCollection')
    z = input('Te gustó la canción? \n' )
    if z == 'si':
        time.sleep(1.5)
        os.system("cls")
        print('Hombre de buen gusto')
        time.sleep(2)
        os.system('cls')
        print('Adiu ;)')
        time.sleep(2)
    else:
        os.system("cls")
        print ('Nos vemos')
        time.sleep(3)

    
elif y == 'no':
    time.sleep(1.5)
    os.system("cls") 
    print('...')
    time.sleep(3)
    os.system("cls") 
    print('Chao')
    time.sleep(2.5)
    os.system("cls")
    time.sleep(1)
    print(';)')
    time.sleep(2)
    os.system("cls")