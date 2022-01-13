class Row():
    def __init__(self, id):
        
        self.cells = list()
        self.id = id

    def addCell(self, cell):
            self.cells.append(cell)

    def validPosition(self, cell):
        return cell.correctRow(self.id)

    def validContent(self, content):
        for eachCell in self.cells:
            if content == eachCell.showContent():
                print("YA EXISTE EL MISMO NUMEMRO EN ESA FILA")
                return False
        return True    
