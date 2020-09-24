#SUDOKU por Manuel Ignacio Cota Casas A01637477
#DESTREZA Abraham Mendoza A01274857
#MEMORAMA Sebastián Escobedo Padilla A01351597
import random
import time
import sys

print("Bienvenido a la Arcade SAM".center(50,"-"))
jugador = input("Cuál es tu nombre? ")

def cls():
    print ("\n" * 100)    

#SUDOKU por Manuel Ignacio Cota Casas A01637477

#Verifica que se pueda usar un numero en una celda
def logicaJuego(ren,col,num,board1):
    checador = 0
    for n in range(0,4):
        if n != col:
            if board1[ren][n] == num:
                checador = 1
                break
    if checador == 0:
        for m in range(0,4):
            if m != ren:
                if board1[m][col] == num:
                    checador = 1
                    break

    if checador == 0:
        if ren <= 1:
            if col <= 1:
                for x in range(0,2): #Checar si el numero esta en el primer cuadrante
                    for y in range(0,2):
                        if x != ren and y != col:
                            if num == board1[x][y]:
                                checador = 1
                                break
                    if checador == 1:
                        break
            else:
                for x in range(0,2): #Checar si el numero esta en el segundo cuadrante
                    for y in range(2,4):
                        if x != ren and y != col:
                            if num == board1[x][y]:
                                checador = 1
                                break
                    if checador == 1:
                        break
        else:
            if col <= 1:
                for x in range(2,4): #Checar si el numero esta en el tercer cuadrante
                    for y in range(0,2):
                        if x != ren and y != col:
                            if num == board1[x][y]:
                                checador = 1
                                break
                    if checador == 1:
                        break
            else:
                for x in range(2,4): #Checar si el numero esta en el cuarto cuadrante
                    for y in range(2,4):
                        if x != ren and y != col:
                            if num == board1[x][y]:
                                checador = 1
                                break
                    if checador == 1:
                        break
    return checador

#Crea un board resuelto
def crearBoard(board2):
    for renglon in range(0,4):
        for columna in range(0,4):
            checador1 = 0
            while checador1 == 0:
                num = random.randint(0,3)   #Asignar un numero a la celda
                checador1 = logicaJuego(renglon,columna,num,board2)
                if checador1 == 0:
                    board2[renglon][columna] = num
                    break
                else:
                    checador1 = 0

    return board2

#Elimina 9 valores del board resuelto y lo imprime como el board inicial
def boardInicial():
    board = [
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","X","X","X"],
    ]

    board = crearBoard(board)

    cont = 0

    while cont < 9:
        columna = random.randint(0,3)
        renglon = random.randint(0,3)
        if (board[columna][renglon] != "X"):
            board[columna][renglon] = "X"
            cont += 1

    print("   0    1    2    3")
    for renglon in range(0,4):
        if renglon == 0:
            print("A",board[renglon],"","\n")
        elif renglon == 1:
            print("B",board[renglon],"","\n")
        elif renglon == 2:
            print("C",board[renglon],"","\n")
        elif renglon == 3:
            print("D",board[renglon],"","\n")
    return board

def respuesta(valido):
    renglonvalido = "ABCD"
    cont = 0
    while cont < 9:
        while 1:
            print("Ingresa tu respuesta.")
            renglon = input("Renglon: ")
            if renglon == "A": #Uso reng para que el programa sepa a que valor corresponde cada letra
                reng = 0
            elif renglon == "B":
                reng = 1
            elif renglon == "C":
                reng = 2
            elif renglon == "D":
                reng = 3
            elif renglon ==  "":
                print("La escritura de la respuesta es incorrecta. Intentelo de nuevo.\n")
            columna = int(input("Columna: "))
            numero = int(input("Número: "))
            if (renglon not in renglonvalido or columna < 0 or columna > 3 or numero < 0 or numero > 3 or renglon == "" or columna == "" or numero == "" or renglon == ValueError or columna == ValueError or numero == ValueError): 
                print("La escritura de la respuesta es incorrecta. Intentelo de nuevo.\n")
            if renglon == "" or columna == "" or numero == "":
                print("La escritura de la respuesta es incorrecta. Intentelo de nuevo.\n")
            elif valido[reng][columna] != "X":
                print("Esta celda ya está ocupada. Intentelo de nuevo.\n")
                continue            
            else:
                break

        checador2 = logicaJuego(reng,columna,numero,valido)

        if checador2 == 0:
            print("¡Respuesta correcta!\n")
            valido[reng][columna] = numero
            cont += 1
            for ren in range(0,4):
                    print(valido[ren],"","\n")

        elif checador2 == 1:
            print("Respuesta incorrecta. Intentalo de nuevo.\n")
            continue

        if cont == 9:
            break
    print("¡Felicidades! ¡Ganó el juego!")
    replay = input("Para volver a jugar, ingrese V. Para volver al menú, ingrese M.")
    while True:
        if replay == "V":
            sudoku()
    if replay == "M":
        print("Gracias por jugar. Volviendo al menú...")
        time.sleep(3)
        menu()
    else:
        print("Entrada incorrecta. Intentelo de nuevo.")
        replay = input("Para volver a jugar, ingrese V. Para volver al menú, ingrese M.")

def reglas():
    print("Bienvenido a SUDOKU. Este juego pondrá a prueba tu agudeza mental y razonamiento.")
    print("Las reglas del juego son las siguientes.")
    print("     1. Deberás colocar en cada celda del tablero un número del 0 al 3.(O sea, 0, 1, 2, 3)")
    print("     2. Los números no se deben repetir tanto en las filas, como en las columnas ni en los cuadrantes.")
    print("        Cuadrantes:\n            primer  | segundo\n            --------|--------\n            tercer  | cuarto")
    print("     3. El tablero tiene la siguiente disposición:\n               0 1 2 3 \n             A X X X X \n             B X X X X \n             C X X X X \n             D X X X X \n")
    print("     4. La respuesta se ingresa por renglon, columna y el número que desee poner.")
    print("     5. El juego termina al completar el tablero correctamente.\n")
    print("        ¡Te deseo suerte!\n")

def sudoku():
    print("SUDOKU".center(50,"-"))
    reglas()
    inicio = input("Ingrese I para iniciar el juego o M para regresar al menú. (I/M): ")
    while True:
        if inicio == "I":
            #cls()
            iniciarJuego = boardInicial()
            respuesta(iniciarJuego)
        elif inicio == "M":
            print("Volviendo al menú...")
            time.sleep(3)
            cls()
            menu()
            break
        else:
            print("Entrada incorrecta. Intentelo de nuevo.")
            inicio = input("Ingrese I para iniciar el juego o M para regresar al menú. (I/M): ")


#Abraham Mendoza A01274857


#Resultado de multiplicaciones
def matriz_repaso():
    N=0
    while N==0:
        Ent=int(input("Para comenzar ingresa 1, si quieres salir ingresa 0 "))
        if Ent==1:
            N1=int(input("Ingrese el primer número "))
            N2=int(input("Ingrese hasta donde quiere que llegue el rango "))
            matriz=[]
            Nu=0
            if N2<N1:
                R2= int(input("El segundo rango no puede ser menor, reingresa otro número mayor que el primero "))
                if N2<=9 or N2<R1:
                    BH2=0
                    while BH2==0:
                        N2= int(input("Incorrecto, reingresa un número mayor "))
                        if N2 >=10:
                            BH2=BH2+1
            if N2<N1:
                    N2= int(input("El segundo rango no puede ser menor, reingresa otro número mayor que el primero "))
                    if  N2<N1:
                        BH2=0
                        while BH2==0:
                            N2= int(input("Incorrecto, lee bien las reglas, bien el número de dos digitos "))
                            if N2 >=10:
                                BH2=BH2+1
            if N1==N2:
                N2= int(input("Los rangos no pueden ser iguales, ingrese el último número para tener un rango diferente "))
                if N2==N1:
                    BH2=0
                    while BH2==0:
                        N2= int(input("Incorrecto, ingresa bien el número de dos digitos "))
                        if N2!=N1:
                            BH2=BH2+1
            for i in range(N1, N2+1):
                lista=[]
                for columna in range(1,11):
                    Nu=Nu+i
                    lista.append(Nu)
                matriz.append(lista)
            for renglon in matriz:
                for columna in renglon:
                    print(f"{columna:3d}" , end=" ")
                print()
            
            
            Ent=int(input("Ingresa 1 para volver a Iniciar "))
            
        elif Ent==0:
            cls()
#Suma de puntaje total                   
def resultado(ScoreT):
    if ScoreT==210:
        print("Felicidades has contestado todo bien")
    elif ScoreT>150:
        print("No ha estado mal, pero puedes hacerlo mejor")
    elif Score >=180:
        print("Nada mal, ya casi lo logras")
    else:
        print("Deberías repasar un poco más")
def puntos_finales(ScoreT):
    SetF=print("Tu puntuación final fue de "+ str(ScoreT))
    return SetF


#Instrucciones del juego
ScoreT=0                   
def Juego():
    Iniciador=0
    NomUsuario=input('Bienvenido, por favor ingresa tú nombre ')
    print(""" Hola , """ , NomUsuario)
    print( """
===========================================================================================================================
Bienvenido a /Destreza/, un juego el cual te ayudará a probar tu agilidad al resolver multiplicaciones  de dos dígitos      
que van incrementando su dificultad, las instrucciones son las siguientes:
1.- El juego consta de 3 sets de multiplicaciones las cuales son brindadas de por el usuario.
2.- Los Rangos brindados deben ser mayores a un dígito y no deben ser el mismo, por ejemplo el 9 no será
aceptado y se pedirá el reingreso de otro número (La manera correcta sería si se ingresa 10 y 15)
3.- El primer rango del set,  será de libre elección, pero en el segundo todos deberán ser entradas mayores o iguales a 20 y
el en tercero mayores a 30
4.- Cada set consta de 7 multiplicaciones
5.- Cada respuesta correcta equivale a un total de 10 puntos, siendo total de 210 puntos 
6.- Para repaso, se te dará la opción de ingresar  a un otra sección en la cual te pidirá dos números (por ejemplo 1 y 10) y eso te
mostrará en la consola los resultados de las tablas de multiplicar del rango colocado
7.- Al momento de comenzar a contestar, ingresa la respuesta correcta de acuerdo a la multiplicación,
que se te muestra en la consola (en caso de que ingreses una letra o presiones espacio e
ingreses el número correcto, contará como error)
8.- Logra el puntaje más alto entre tus amigos y demuestrales que eres el mejor
9.- ¡Diviértete!
============================================================================================================================
""")
    while Iniciador==0:

#Inicio del juego
        Inicio= int(input("""Ingresa 1 para iniciar, 2 para practicar un rango de multiplicaciones
dando por usted y 0 para cerrar el juego """))
        if Inicio==1:
            ScoreT=0
            R1= int(input("Ingresa el primer número del rango "))
            if R1<=9:
                BH=0
                while BH==0:
                    R1= int(input("Incorrecto, lee bien las reglas, ingresa un número de dos digitos "))
                    if R1>=10:
                        BH=BH+1
            R2=int(input("Ingrese el número hasta el que quiere que llegue el rango "))
            if R2<=9:
                BH2=0
                while BH2==0:
                    R2= int(input("Incorrecto, lee bien las reglas, ingresa un número de dos digitos "))
                    if R2 >=10:
                        BH2=BH2+1
            if R2<R1:
                R2= int(input("El segundo rango no puede ser menor, reingresa otro número mayor que el primero "))
                if R2<=9 or R2<R1:
                    BH2=0
                    while BH2==0:
                        R2= int(input("Incorrecto, lee bien las reglas, bien el número de dos digitos "))
                        if R2 >=10:
                            BH2=BH2+1
            if R1==R2:
                R2= int(input("Los rangos no pueden ser iguales, ingrese el último número para tener un rango diferente "))
                if R2<=9 or R2==R1:
                    BH2=0
                    while BH2==0:
                        R2= int(input("Incorrecto, ingresa bien el número de dos digitos "))
                        if R2 >=10 and R2!=R1:
                            BH2=BH2+1
            print('Inicia Set de multiplicaciones de' ,R1, 'a' , R2)
            Contador=0
            Score=0
            for i in range(1,8):
                No=random.randint(R1 , R2)
                No2= random.randint(1,10)
                Multi=input(str(No)+ "*"+str(No2)+"= ")
                if Multi == str(No*No2):
                    ScoreT=ScoreT+10
                    Score=Score+10
                    Contador=Contador+1
                    print("Correcto")
                else:
                    print("Incorrecto")
                    Contador= Contador+1
            Set1=Score
            Set1P=print("Tu puntuación final en este primer set fue de " + str(Score))
            
            
            Continuar=int(input( "Para continuar al siguiente set, ingresa 2 "))
            if Continuar==2:
                R3= int(input("Ingresa el primer número del rango "))
                if R3<=19:
                    BH=0
                    while BH==0:
                        R3= int(input("Incorrecto, lee bien las reglas, ingresa un número mayor o igual a 20 "))
                        if R3 >=19:
                            BH=BH+1
                R4=int(input("Ingrese el número hasta el que quiere que llegue el rango "))
                if R4<=19:
                    BH2=0
                    while BH2==0:
                        R4= int(input("Incorrecto, ingresaste un número de un digito o menor a la primer entrada "))
                        if R4 >=20:
                            BH2=BH2+1
                if R4<R3:
                    R4= int(input("El segundo rango no puede ser menor, reingresa otro número mayor que el primero "))
                    if R4<=19 or R4<R3:
                        BH2=0
                        while BH2==0:
                            R4= int(input("Incorrecto, lee bien las reglas, ingresa bien el número "))
                            if R4 >=20:
                                BH2=BH2+1
                if R3==R4:
                    R4= int(input("Los rangos no pueden ser iguales, ingrese el último número para tener un rango diferente "))
                    if R3<=19 or R4==R3:
                        BH2=0
                        while BH2==0:
                            R4= int(input("Incorrecto, ingresa bien el número de dos digitos "))
                            if R4 >=20 and R4!=R3:
                                BH2=BH2+1
                print('Inicia Set de multiplicaciones de' ,R3, 'a' , R4)
                Contador2=0
                Score2=0
                for i in range(1,8):
                    No=random.randint(R3 , R4)
                    No2= random.randint(1,10)
                    Multi=input(str(No)+ "*"+str(No2)+"= ")
                    if Multi == str(No*No2):
                        ScoreT=ScoreT+10
                        Score2= Score2+10
                        Contador2=Contador2+1
                        print("Correcto")
                    else:
                        print("Incorrecto")
                        Contador2= Contador2+1
            Set2= Score2
            Set2P=print("Tu puntuación final en este segundo set fue de " + str(Score2))
                
            Continuar2= int(input("Ingresa 3 para iniciar el último set, cuidado el más difícil "))
            if Continuar2==3:
                R5= int(input("Ingresa el primer número del rango "))
                if R5<=29:
                    BH=0
                    while BH==0:
                        R5= int(input("Incorrecto, lee bien las reglas, ingresa un número mayor o igual a 30 "))
                        if R5 >=29:
                            BH=BH+1
                R6=int(input("Ingrese el número hasta el que quiere que llegue el rango "))
                if R6<=19:
                    BH2=0
                    while BH2==0:
                        R6= int(input("Incorrecto, ingresaste un número de un digito o menor a la primer entrada "))
                        if R6 >=20:
                            BH2=BH2+1
                if R6<R5:
                    R6= int(input("El segundo rango no puede ser menor, reingresa otro número mayor que el primero "))
                    if R6<=19 or R6<R5:
                        BH2=0
                        while BH2==0:
                            R6= int(input("Incorrecto, lee bien las reglas, ingresa bien el número "))
                            if R6 >=20:
                                BH2=BH2+1
                if R5==R6:
                    R6= int(input("Los rangos no pueden ser iguales, ingrese el último número para tener un rango diferente "))
                    if R5<=29 or R6==R5:
                        BH2=0
                        while BH2==0:
                            R6= int(input("Incorrecto, ingresa bien el número de dos digitos "))
                            if R6 >=20 and R6!=R5:
                                BH2=BH2+1
                print('Inicia Set de multiplicaciones de' ,R5, 'a' , R6)
                Contador3=0
                Score3=0
                for i in range(1,8):
                    No=random.randint(R5 , R6)
                    No2= random.randint(1,10)
                    Multi=input(str(No)+ "*"+str(No2)+"= ")
                    if Multi == str(No*No2):
                        Score3=Score3+10
                        ScoreT=ScoreT+10
                        Contador3=Contador3+1
                        print("Correcto")
                    else:
                        print("Incorrecto")
                        Contador3= Contador3+1
                Set3= Score3
                Set3P=print("Tu puntuación final en este último set fue de " + str(Score3))
                puntos_finales(ScoreT)
                resultado(ScoreT)
                H=int(input("Para volver a inicio, ingresa 1 "))
                if H==1:
                    print("\n"*20)
        
      

    

        elif Inicio==2:
         matriz_repaso()
            
        else:
            break
#Sebastián Escobedo Padilla A01351597
puntos_del_jugador_1= 0
matriz =[[" ","0","1","2","3","4","5"],["0","-","-","-","-","-","-"],["1","-","-","-","-","-","-"],["2","-","-","-","-","-","-"],["3","-","-","-","-","-","-"],["4","-","-","-","-","-","-"],["5","-","-","-","-","-","-"]]
num_1 = [0,0,0,0,0,0]
num_2 = [0,0,0,0,0,0]
num_3 = [0,0,0,0,0,0]
num_4 = [0,0,0,0,0,0]
num_5 = [0,0,0,0,0,0]
num_6 = [0,0,0,0,0,0]
checarNum = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
checarCarta = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def tablero():
    print ("Puntos"+ ":" + " " + str(puntos_del_jugador_1))
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in matriz]))
    
def generar_numeros ():
    for i in range (6):
        num_1 [i] = str(random.randrange(4,6))
        while (checarNum[int(num_1 [i])] == 2 ):
            num_1 [i] = str(random.randrange(4,6))
    for i in range (6):
        num_2 [i] = str(random.randrange(13,15))
        while (checarNum[int(num_2 [i])] == 2 ):
            num_2 [i] = str(random.randrange(13,15))
    for i in range (6):
        num_3 [i] = str(random.randrange(1,3))
        while (checarNum[int(num_3 [i])] == 2 ):
            num_3 [i] = str(random.randrange(1,3))
    for i in range (6):
        num_4 [i] = str(random.randrange(7,9))
        while (checarNum[int(num_4 [i])] == 2 ):
            num_4 [i] = str(random.randrange(7,9))
    for i in range (6):
        num_5 [i] = str(random.randrange(15,18))
        while (checarNum[int(num_5 [i])] == 2 ):
            num_5 [i] = str(random.randrange(15,18))
    for i in range (6):
        num_6 [i] = str(random.randrange(10,12))
        while (checarNum[int(num_6 [i])] == 2 ):
            num_6 [i] = str(random.randrange(10,12))

def game ():
    print( """

Bienvenido al juego de Memorama
1.- El juego consta de diferentes cartas volteadas en el cuál tienes que encontrar el
mismo para de números para sumar puntos
2.- Para seleccionar una carta deberás poner dos números pegados
3.- Primero el número de columna y después el número de fila
4.- Por ejemplo 00 para casilla de la esquina superior izquierda ó 50 para la esquina superior derecha
5.- Al juntar 5 pares ganas el juego, esto debido a la dificultad que suele ser unas veces en recordar las casillas
6.- Escriba menu (en minúsculas y sin acento) para regresar al menú del juego
7.- Escriba salir (en minúsculas) cuando quiera terminar el juego
8.- ¡Diviertete!


""")
    global puntos_del_jugador_1
    tablero ()
    generar_numeros()
    turno = 1
    while puntos_del_jugador_1 != 9 or not puntos_del_jugador_1 == 8:
        select1 = checarCarta(turno)
        select2 = checarCarta(turno)
        if (matriz[int(select1[1])+1][int(select1[0])+1] == matriz[int(select2[1])+1][int(select2[0])+1]):
            if turno == 1 or (turno == 2):
                puntos_del_jugador_1 += 1
        else :
            matriz[int(select1[1])+1][int(select1[0])+1] = "-"
            matriz[int(select2[1])+1][int(select2[0])+1] = "-"
           
        
        if (turno == 1):
            turno = 2
        else:
            turno = 1
        tablero()

        if(puntos_del_jugador_1 == 5):
            print("Felicidades," + (jugador) + " haz ganado")
            sys.exit()

    
def checarCarta(turno):
    x = input((jugador)+ " " + "seleccione una carta: ")
    comprobar = list(str(x))
    if x == "salir":
        sys.exit()
    elif x == "menu":
        menu()
    while (int(comprobar[0]) > 5 or int(comprobar[1]) > 5):
        x = input("Seleccione otra carta: ")
        comprobar = list(x)
    while (matriz [int(comprobar[1])+1][int(comprobar[0])+1] != "-"):
        x = input("Seleccione otra carta: ")
        comprobar = list(x)
    
    if (comprobar [1] == "0"):
        matriz [int(comprobar[1])+1][int(comprobar[0])+1] = str(num_1[int(comprobar[0])])
    elif (comprobar [1] == "1"):
        matriz [int(comprobar[1])+1][int(comprobar[0])+1] = str(num_2[int(comprobar[0])])
    elif (comprobar [1] == "2"):
        matriz [int(comprobar[1])+1][int(comprobar[0])+1] = str(num_3[int(comprobar[0])])
    elif (comprobar [1] == "3"):
        matriz [int(comprobar[1])+1][int(comprobar[0])+1] = str(num_4[int(comprobar[0])])
    elif (comprobar [1] == "4"):
        matriz [int(comprobar[1])+1][int(comprobar[0])+1] = str(num_5[int(comprobar[0])])
    elif (comprobar [1] == "5"):
        matriz [int(comprobar[1])+1][int(comprobar[0])+1] = str(num_6[int(comprobar[0])])
    tablero()
    return comprobar 
    


def menu():
    print("¡Hola",jugador,", ven a divertirte con estos fabulosos juegos!\n \n     1. SUDOKU\n")
    print("     2. Destreza\n")
    print("     3. Memorama\n")
    start = int(input("Seleccione el juego de su elección ingresando el número: "))
    if start == 1:
        sudoku()
    elif start == 2:
        Juego()
    elif start == 3:
        game()
    else:
        print("Error. Debes ingresar un número entre 1 y 3.")
        print("\n"*5)
        menu()

menu()
