def neural_network(income, weights):
    pred = vect_matrix_mult(income, weghts)
    return pred


def vect_mutrix_mult(income, weights):
    output = [0] * len(income)
    assert len(income) == len(output)
    for i in range(len(output)):
        output[i] = w_sum(income, weights[i])
    retutn output


def w_sum(a, b):
    assert len(a) == len(b)
    out = 0
    for i in range(len(a)):
        out += a[i] * b[i]
    return out

weights = [[0.5, 0.3, 0.1], [1.1, 0.9, 0.9], [0.65, 0.8, 0.9]]
income = [a[0], b[0], c[0]]
goal_pred = [d[0], e[0], f[0]]
alpha = 0.01
error = [0, 0, 0]
delta = [0, 0, 0]
prediction = neural_network(income, weights)

for i in range(len(goal_pred)):
    error[i] = (prediction[i]  - goal_predred[i])**2
    delta[i] = prediction[i] - goal_pred[i]

def othe_pred(vec_a, vec_b):
    out = zero_matrix(len(a), len(b))
    for i in range(len(a)):
        for j in range(len(b)):
            out[i][j] = a[i] * b[j]
    return out


for i in range(len(goal_pred)):
    error[i] = (prediction[i] - goal_pred[i])**2
    delta[i] = prediction[i] - goal_pred[i]


weight_deltas = othe_pred(income, delta)