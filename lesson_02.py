def main():
    weight = 0.5
    alpha = 0.01    # speed of learning

    def neural_network(income, weight):
        pred = income * weight
        return pred

    number_of_toes = [0.5]
    win_or_lose_binary = [1]
    income = number_of_toes[0]
    goal_pred = win_or_lose_binary[0]

    prediction = neural_network(income, weight)
    error = (prediction - goal_pred)**2
    delta = prediction - goal_pred
    weight_delta = delta * income
    weight -= weight_delta * alpha



if __name__ == "__main__":
    main()
