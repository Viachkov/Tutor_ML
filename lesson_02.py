def main():
    weight = 0.5
    goal_pred = 0.8
    income = 2 
    alpha = 0.1

    for i in range(20):
        prediction = income * weight
        error = (prediction - goal_pred)**2
        derivate = (prediction - goal_pred) * income
        weight -= derivate * alpha

        print('Error: ' + str(error) + ' Prediction: ' + str(prediction))



if __name__ == "__main__":
    main()
