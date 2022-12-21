class Queen:
    position_queens = []
    
    def __init__(self, row, column):
        if row < 0:
            raise ValueError("row not positive")
        if row > 7:
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        if column > 7:
            raise ValueError("column not on board")
        aux = (row, column)
        if aux in Queen.position_queens:
            raise ValueError("Invalid queen position: both queens in the same square")
        self.position = aux
        Queen.position_queens.append(aux)

    def can_attack(self, another_queen):
        Queen.position_queens.clear()
        queen1 = (row, column) = self.position
        queen2 = (row, column) = another_queen.position
        if queen1[0] == queen2[0] or queen1[1] == queen2[1]:
            return True
        if (queen1[0] - queen2[0])**2 == (queen1[1] - queen2[1])**2:
            return True
        return False
