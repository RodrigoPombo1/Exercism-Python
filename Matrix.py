class Matrix:
    def __init__(self, matrix_string):
        self.matrix = []
        matrix_row_div = matrix_string.split("\n")
        for counter, row in enumerate(matrix_row_div):
            self.matrix.append([])
            row = matrix_row_div[counter].split(" ")
            for element in row:
                self.matrix[counter].append(int(element))
    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        res = []
        for row in self.matrix:
            res.append(row[index - 1])
        return res
