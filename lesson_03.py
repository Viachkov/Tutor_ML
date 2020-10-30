def main():

    weights = [[0.1, 0.1, -0.3],
                [0.1, 0.2, 0.0],
                [0.0, 1.3, 0.1]]
    
    def w_sum(a, b):
        assert len(a) == len(b)
        out = 0
        for i in range(len(a)):
            out += a[i] * b[i]
        return out


    def vect_mat_mult(vector, matrix):
        output = [0, 0, 0]
        assert len(vector) == len(matrix)
        for i in range(len(vector)):
            output[i] = w_sum(vector, matrix[i])
        return output


    def neural_network(income, weights):
        pred = vect_mat_mult(income, weights)
        return pred
    
    toes = [8.5, 9.5, 9.9, 9.0]
    wlrec = [0.65, 0.8, 0.8, 0.9]
    nfans = [1.2, 1.3, 0.5, 1.0]

    hurt = [0.1, 0.0, 0.0, 0.1]
    win = [1, 1, 0, 1]
    sad = [0.1, 0.0, 0.1, 0.2]

    alpha = 0.01

    income = [toes[0], wlrec[0], nfans[0]]
    goal_prediction = [hurt[0], win[0], sad[0]]

    prediction = neural_network(income, weights)

    error = [0, 0, 0]
    delta = [0, 0, 0]

    for i range(len(goal_prediction)):
        error[i] = (prediction[i] - goal_prediction[i]**2)
        delta = prediction[i] - goal_prediction[i]

    
    def other_prod(vec_a, vec_b):
        out = zero_matrix(len(a), len(b))

        for i in range(len(a)):
            for j in range(len(b)):
                out[i][j] = a[i] * b[j]
        return out

    
    income = [toes[0], wlrec[0], nfans[0]]
    goal_prediction = [hurt[0], win[0], sad[0]]

    for i in range(len(goal_prediction)):
        error[i] = (prediction[i] - goal_prediction[i])**2
        delta[i] = prediction[i] - goal_prediction[i]

    weight_deltas = other_prod(income, delta)


if __name__ == "__main__":
    main()
