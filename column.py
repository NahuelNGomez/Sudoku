class Column():
    def __init__(self, id):

        self.cells = list()
        self.id = id

    def addCell(self, cell):
            self.cells.append(cell)
  
    def validPosition(self, cell):
        return cell.correctColumn(self.id)

    def validContent(self, content):
        for eachCell in self.cells:
 
            print(eachCell.showContent())
            if content == eachCell.showContent():
                print("YA EXISTE EL MISMO NUMERO EN ESA COLUMNA")
                return False
        return True