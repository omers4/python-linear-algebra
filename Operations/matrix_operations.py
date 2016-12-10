from Objects import matrix
from Objects import field
from Objects.Errors import matrix_operation_illegal_exception as errors

__author__ = 'Omer'


def get_multiply_cell_value(field, row_index, column_index, matrix_1, matrix_2):
    """
    :type field: field.Field
    :type row_index: int
    :type column_index: int
    :type matrix_1: matrix.Matrix
    :type matrix_2: matrix.Matrix
    :type modulo: int
    :rtype: int
    """
    row_cells_list = matrix_1.get_row(row_index)
    column_cells_list = matrix_2.get_column(column_index)

    cell_value = 0

    for n in range(len(row_cells_list)):
        mul = field.mul(row_cells_list[n], column_cells_list[n])
        cell_value = field.sum(cell_value, mul)

    return cell_value


def multiply_matrix(field, matrix_1, matrix_2, modulo=1):
    """
    :type field: field.Field
    :type matrix_1: matrix.Matrix
    :type matrix_2: matrix.Matrix
    :type modulo: int
    :rtype: matrix.Matrix
    """
    if not matrix_1.column_size == matrix_2.row_size:
        errors.MatrixOperationIllegal("Operation is illegal")

    new_matrix = matrix.EmptyMatrix(field, (matrix_1.row_size, matrix_2.column_size))

    for row_index in range(matrix_1.row_size):
        for column_index in range(matrix_2.column_size):
            cell_value = get_multiply_cell_value(field, row_index, column_index, matrix_1, matrix_2)
            new_matrix.set_cell(row_index, column_index, cell_value)
    return new_matrix
