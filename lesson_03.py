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





if __name__ == "__main__":
    main()