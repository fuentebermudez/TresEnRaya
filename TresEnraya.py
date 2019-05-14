

def getNumeroDeJugadores():
    pass


def inicializaTablero():
    tableroZero = [["-","-","-"], ["-","-","-"], ["-","-","-"]]
    
    return tableroZero

def dibujaTablero(tableroMast):
    for fila in tableroMast:
        filaTablero=""
        for columna in fila:
            filaTablero=filaTablero+ " | " + columna + " |"
        print(filaTablero)

tableroZero = inicializaTablero()
dibujaTablero(tableroZero)

tableroZero = [["X","X","X"], ["O","X","-"], ["-","-","X"]]

def getFilas(tablero):
    filas=[fila for fila in tablero]
    return filas

def getColumnas(tablero):
    columna=[]
    columnas=[]
    for columna in range(3):
        for fila in range(3):
           print( tablero[fila][columna])
    return columnas
 
getColumnas(tableroZero)

def checkFila(fila):
    victoria=0
    filaUnicos=set(fila)
    if len(filaUnicos)==1:
        victoria=1
    return victoria



    pass
def checkVitoria(tablero):
    for fila in tablero:
        victoria=checkFila(fila)
        print(victoria)


checkVitoria(tableroZero)
