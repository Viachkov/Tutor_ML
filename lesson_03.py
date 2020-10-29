def main():

    weights = [0.3, 0.2, 0.9]

    def neural_network(income, weights):
        pred = scalar_ele_mul(income, weights)
        return pred


    def scalar_ele_mul(number, vector):
        output = [0, 0, 0]
        assert len(output) == len(vector)
        for i in range(len(vector)):
            output[i] = number * vector[i]
        return output


    wlrec = [0.65, 1.0, 1.0, 0.9]
    hurt = [0.1, 0.0, 0.0, 0.1]
    win = [1, 1, 0, 1]
    sad = [0.1, 0.0, 0.1, 0.2]

    income = wlrec[0]
    goal_pred = [hurt[0], win[0], sad[0]]

    prediction = neural_network(income, weights)

    error = [0, 0, 0]
    delta = [0, 0, 0]

    for i in range(len(goal_pred)):
        error[i] = (prediction[i] - goal_pred[i])**2
        delta[i] = prediction[i] - goal_pred[i]

    weight_deltas = scalar_ele_mul(income, weights)
    alpha = 0.01

    for i in range(len(weights)):
        weights[i] -= weight_deltas[i] * alpha

    print('Weights: ' + str(weights))
    print('Weight-delta: ' + str(weight_deltas))



    



if __name__ == "__main__":
    main()
