def main():
    def w_sum(a, b):
        assert len(a) == len(b)
        output = 0
        for i in range(len(a)):
            output += a[i] * b[i]
        return output

    def mult_elem(number, vector):
        output = [0, 0, 0]
        assert len(vector) == len(output)
        output = [0, 0, 0]
        for i in range(len(vector)):
            output[i] = number * vector[i]
        return output

    weights = [0.1, 0.2, -.1]

    def neural_network(income, weights):
        pred = w_sum(income, weights)
        return pred

    toes = [8.5, 9.5, 9.9, 9.0]
    wlrec = [0.65, 0.8, 0.8, 0.9]
    nfans = [1.2, 1.3, 0.5, 1.0]

    win_or_lose = [1, 1, 0, 1]
    true = win_or_lose[0]
    income = [toes[0], wlrec[0], nfans[0]]


    prediction = neural_network(income, weights)
    error = (prediction - true)**2
    delta = prediction - true
    weights_delta = mult_elem(delta, income)
    alpha = 0.01

    for i in range(len(weights)):
        weights[i] -= alpha* weights_delta[i]
    
    print('Weights: ' + str(weights) + ' Weights_delta: ' + str(weights_delta))


if __name__ == "__main__":
    main()
