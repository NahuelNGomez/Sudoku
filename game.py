from board import * 

class Game():
    def __init__(self):
        self.board = Board()
       # self.board.showAllPositions()
    
    def addContent(self, row, column, content):
        self.board.addContent(row, column, content)
        self.board.showBoard()

    def verifyStatus(self):

        if self.board.noEmptyPosition():
            self.board.verify()
        else:
            return False   