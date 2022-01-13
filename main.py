from game import * 

def requestNumber(game): 

    valid = 1
    first = 1
    while (not valid == 0) or (first == 1):
        valid = 0
        number = int(input("diga numero: "))
        row = int(input("diga fila: "))
        column = int(input("diga columna: "))
        
        if number < 1 or number > 9:
            print("El numero debe ser entre 1 y 9")
            valid = valid + 1
        if(row < 1 or row > 9):
            print(("La fila debe ser entre 1 y 9"))
            valid = valid + 1
        if(column < 1 or column > 9):
            print(("La columna debe ser entre 1 y 9"))     
            valid = valid + 1
        #if(numberAlreadySetInColumn() or numberAlreadySetInRaw() or numberAlreadySetInRaw()):
         #   print((" ya existe un numero en la misma fila, posicion o grupo"))     
          #  valid = valid + 1
        first = 0
    game.addContent(row, column, number)

def jugar():
    print("empieza el juego")
    game = Game()
    noWinner = True
    while noWinner:
        requestNumber(game)
     #   noWinner = game.verifyStatus()




jugar()