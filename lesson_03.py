def main():
    def w_sum(a, b):
        assert len(a) == len(b)
        output = 0
        for i in range(len(a)):
            output += a[i] * b[i]
        return output

    weights = [0.1, 0.2, -1]

    def neural_network(income, weights):
        pred = w_sum(income, weights)
        return pred

    toes = []
    wlrec = []
    nfans = []

    win_or_lose = []
    true = win_or_lose
    income = [toes[0], wlrec[0], nfans[0]]


    prediction = neural_network(income, weights)
    error = (prediction - true)**2
    delta = prediction - true





if __name__ == "__main__":
    main()