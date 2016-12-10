from copy import deepcopy
from Objects.field import Field

__author__ = 'Omer'


class Matrix(object):
    def __init__(self, field, rows):
        """
        :type field: Field
        :type rows: list
        """
        self._field = field
        self._rows = rows

    @property
    def size(self):
        """
        :rtype: tuple
        """
        return len(self._rows), len(self._rows[0])

    def get_row(self, row_index):
        """
        :type row_index: int
        :rtype: list
        """
        return self._rows[row_index]

    def get_column(self, column_index):
        """
        :type row_index: int
        :rtype: list
        """
        return [row[column_index] for row in self._rows]

    @property
    def row_size(self):
        """
        :rtype: int
        """
        return self.size[0]

    @property
    def column_size(self):
        """
        :rtype: int
        """
        return self.size[1]

    def pop_row(self, row_index):
        """
        :type row_index: int
        """
        self._rows.pop(row_index)

    def pop_column(self, column_index):
        """
        :type column_index: int
        """
        [row.pop(column_index) for row in self._rows]

    def _get_minor_matrix(self, row_index, column_index):
        """
        :type row_index: int
        :type column_index: int
        :rtype: Matrix
        """
        minor_matrix = deepcopy(self)
        minor_matrix.pop_row(row_index)
        minor_matrix.pop_column(column_index)
        return minor_matrix

    def get_determinant(self, by_row, minor_matrix=None):
        """
        :type minor_matrix: Matrix
        :rtype: int
        """

        if None == minor_matrix:
            minor_matrix = self

        if minor_matrix.row_size == 2:
            major_diagonal = self._field.mul(minor_matrix._rows[0][0], minor_matrix._rows[1][1])
            minor_diagonal = self._field.mul(minor_matrix._rows[0][1], minor_matrix._rows[1][0])

            return self._field.sub(major_diagonal, minor_diagonal)

        return self._field.sum(
            *
            [self._field.mul(self._field.mul(self._field.pow(self._field.get_negative(1), j + 1 + by_row + 1),
                                             self.get_row(by_row)[j]),
                             self.get_determinant(by_row, self._get_minor_matrix(by_row, j)))
             for j in range(self.column_size)])


    def set_cell(self, row_index, column_index, cell_value):
        self._rows[row_index][column_index] = cell_value

    def __str__(self):
        return 'Matrix - {}x{}\n'.format(self.row_size, self.column_size) + \
               '\n'.join(['|' + ' '.join([str(cell) for cell in row]) + '|' for row in self._rows]) + '\n\n'


class EmptyMatrix(Matrix):
    def __init__(self, field, size):
        super(EmptyMatrix, self).__init__(field, [])
        self._field = field
        self._size = size
        self._init_matrix()

    def _init_matrix(self):
        for i in range(self._size[0]):
            self._rows.append([])
            for j in range(self._size[1]):
                self._rows[i].append(None)