# python-linear-algebra
Various operations from the world of Linear Algebra

### Easily create matrices and operate basic actions above them

##### Generic Matrix
```
rows = [[1, 2, 3],
        [3, 1, 2],
        [2, 3, 1]]
field = real_field.RealField()
matrix_1 = matrix.Matrix(field, rows)
```

##### Create a Matrix with Modulo field
```
field = real_field.RealField(modulo=7)
```

##### Multiply Matrices
```
matrix_operations.multiply_matrix(field, matrix_1, matrix_2)
```

##### Get Determinant
```
matrix_2.get_determinant(0)
```

##### Get Matrix Representation
```
print matrix_1
```

Output:
```
Matrix - 3x3
|1 0 0|
|0 1 0|
|0 0 1|
```
