from types import new_class
from row import *
from column import *
from position import *


class Board():
    def __init__(self):

        self.positions = list()
        self.groups = list()
        self.rows = list()
        self.columns = list()
        self.initializePositions()
        self.initializeRowsAndColumns()


    def initializeRowsAndColumns(self):
        for i in range(1, 10):
            newRow = Row(i)
            newColumn = Column(i)
            self.columns.append(newColumn)
            self.rows.append(newRow)

    def initializePositions(self):
        
        for i in range(1, 10):
            for j in range(1,10):

                newPosition = Position(i,j)
                self.positions.append(newPosition)

    def searchRow(self, position):
        searchedRow = None
        for row in self.rows:
            if row.validPosition(position):
                searchedRow = row
                break
        return searchedRow   

    def searchColumn(self, position):
        searchedColumns = None
        for column in self.columns:
            if column.validPosition(position):
                searchedColumns = column
                break
        return searchedColumns     

    def validContentOfRowAndColumn(self, row, column, content):
        return (row.validContent(content) and column.validContent(content))

    def addInRowAndColumnList(self, position, content):
        row = self.searchRow(position)
        column = self.searchColumn(position)
        if self.validContentOfRowAndColumn(row, column, content):

            row.addCell(position)
            column.addCell(position)
            return True
        return False

    def showBoard(self):
        accountant = 0
        print("┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐")
        print("│   │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │")
        print("├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")
        print("│ A │ ", end="")
        for position in self.positions:
            if accountant < 9:
                if(accountant == 2 or accountant == 5):
                    print(str(position.showContent()) +" █ ", end="" )
                else:
                    print(str(position.showContent()) +" │ ", end="" )
            accountant = accountant + 1
        print(" ")
        print("├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")

        print("│ B │ ", end="")
        accountant = 0
        for position in self.positions:
            if accountant > 8 and accountant < 18:
                if(accountant == 11 or accountant == 14):
                    print(str(position.showContent()) +" █ ", end="" )
                else:
                    print(str(position.showContent()) +" │ ", end="" )
            accountant = accountant + 1
        print(" ")
        print("├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")

        print("│ C │ ", end="")
        accountant = 0
        for position in self.positions:
            if accountant > 17 and accountant < 27:
                if(accountant == 20 or accountant == 23):
                    print(str(position.showContent()) +" █ ", end="" )
                else:
                    print(str(position.showContent()) +" │ ", end="" )

            accountant = accountant + 1
        print(" ")
        print("├■■■┼■■■┼■■■┼■■■┼■■■┼■■■┼■■■┼■■■┼■■■┼■■■┤")

        print("│ D │ ", end="")
        accountant = 0
        for position in self.positions:
            if accountant > 26 and accountant < 36:
                if(accountant == 29 or accountant == 32):
                    print(str(position.showContent()) +" █ ", end="" )
                else:
                    print(str(position.showContent()) +" │ ", end="" )

            accountant = accountant + 1
        print(" ")
        print("├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")

        print("│ E │ ", end="")
        accountant = 0
        for position in self.positions:
            if accountant > 35 and accountant < 45:
                if(accountant == 38 or accountant == 41):
                    print(str(position.showContent()) +" █ ", end="" )
                else:
                    print(str(position.showContent()) +" │ ", end="" )
            accountant = accountant + 1
        print(" ")
        print("├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")

        print("│ F │ ", end="")
        accountant = 0
        for position in self.positions:
            if accountant > 44 and accountant < 54:
                if(accountant == 47 or accountant == 50):
                    print(str(position.showContent()) +" █ ", end="" )
                else:
                    print(str(position.showContent()) +" │ ", end="" )
            accountant = accountant + 1
        print(" ")
        print("├■■■┼■■■┼■■■┼■■■┼■■■┼■■■┼■■■┼■■■┼■■■┼■■■┤")

        print("│ G │ ", end="")
        accountant = 0
        for position in self.positions:
            if accountant > 53 and accountant < 63:
                if(accountant == 56 or accountant == 59):
                    print(str(position.showContent()) +" █ ", end="" )
                else:
                    print(str(position.showContent()) +" │ ", end="" )
            accountant = accountant + 1
        print(" ")
        print("├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")

        print("│ H │ ", end="")
        accountant = 0
        for position in self.positions:
            if accountant > 62 and accountant < 72:
                if(accountant == 65 or accountant == 68):
                    print(str(position.showContent()) +" █ ", end="" )
                else:
                    print(str(position.showContent()) +" │ ", end="" )
            accountant = accountant + 1
        print(" ")
        print("├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")

        print("│ I │ ", end="")
        accountant = 0
        for position in self.positions:
            if accountant > 71:
                if(accountant == 74 or accountant == 77):
                    print(str(position.showContent()) +" █ ", end="" )
                else:
                    print(str(position.showContent()) +" │ ", end="" )
            accountant = accountant + 1
        print(" ")
        print("└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘")


    def addContent(self, row, column, content):
        position = self.searchPosition(row,column)
        if self.addInRowAndColumnList(position, content):
            position.addContent(content)
        
   

    def searchPosition(self, row, column):
        for position in self.positions:
            if position.isCorrectPosition(row,column):
                return position

    def noEmptyPosition(self):
        empty = 0
        for position in self.positions:
            if position.isEmpty():
                empty = empty + 1
        return empty == 0


  #  def verify(self):
        verifyRow
        verifyColumns
        VerifyGroups
