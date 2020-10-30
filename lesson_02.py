    def main():
    weight = 0.5
    alpha = 0.01    # speed of learning
    goal_pred = 0.8
    income = 2 
    alpha = 0.1

    def neural_network(income, weight):
        pred = income * weight
        return pred
    for i in range(20):
        prediction = income * weight
        error = (prediction - goal_pred)**2
        derivate = (prediction - goal_pred) * income
        weight -= derivate * alpha

    number_of_toes = [0.5]
    win_or_lose_binary = [1]
    income = number_of_toes[0]
    goal_pred = win_or_lose_binary[0]

    prediction = neural_network(income, weight)
    error = (prediction - goal_pred)**2
    delta = prediction - goal_pred
    weight_delta = delta * income
    weight -= weight_delta * alpha
        print('Error: ' + str(error) + ' Prediction: ' + str(prediction))



if __name__ == "__main__":
    main()
