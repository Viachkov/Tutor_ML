def main():
    weight = 0.5
    income = 0.5
    goal_prediction = 0.8

    step_amount = 0.001

    for iteration in range(1101):
        prediction = income * weight
        error = (goal_prediction - prediction)**2

        print('error:' + str(error) + ' | Prediction: ' + str(prediction))

        prediction_up = income * (weight + step_amount)
        error_up = (goal_prediction - prediction_up)**2

        prediction_down = income * (weight - step_amount)
        error_down = (goal_prediction - prediction_down)**2

        if error_down < error_up:
            weight -= step_amount
        
        if error_up < error_down:
            weight += step_amount
    



if __name__ == "__main__":
    main()
