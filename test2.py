def zero_matrix(row, colons):
    out = [([0] * row) for i in range(colons)]
    return out

# test matrix
a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]


def add_matrix(vec_a, vec_b):
    out = zero_matrix(len(a[0]), len(a))
    for i in range(len(a)):
        for j in range(len(a[0])):
            out[i][j] = a[i][j] + b[i][j]
    return out

matrix_test = add_matrix(a, b)
print('Matrix add: ', matrix_test)

def substruct_matrix(vec_a, vec_b):
    out = zero_matrix(len(a[0]), len(a))
    for i in range(len(a)):
        for j in range(len(a[0])):
            out[i][j] = a[i][j] - b[i][j]
    return out

matrix_sub = substruct_matrix(a, b)
print('Subctruct matrx: ', matrix_sub)



def multiplication_matrix(a, b):
    r = []
    m = []
    for i in range(len(a)):
        for j in range(len(b[0])):
            sums = 0
            for k in range(len(b)):
                sums = sums + (a[i][k] *  b[k][j])
            r.append(sums)
        m.append(r)
        r = []
    return m

matrix = multiplication_matrix(a, b)
print('matrix: ', matrix)
