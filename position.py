class Position():
    def __init__(self, row, column):

        self.row = row
        self.column = column
        self.content = None
       
    def addContent(self, content):

        self.content = content

    def isCorrectPosition(self, row, column):
        if self.column == column and self.row == row:
            return True    

    def showContent(self):
        if self.content == None:
            return "-"
        return self.content

    def isEmpty(self):
        return self.content == None

    def correctRow(self, id):
        return self.row == id

    def correctColumn(self, id):
        return self.column == id    
