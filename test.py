weight, goal_pred, income = (0.0, 0.8, 1.1) 

for iteration in range(4):
    prediction  = income * weight
    error = (prediction - goal_pred)**2
    delta = prediction - goal_pred
    weight_delta = delta * income
    weight -= weight_delta

    print('Error: ' + str(error) + ' Prediction: ' + str(prediction))
    print('Weight: ' + str(weight))
    print('Delta: ' + str(delta) + ' Weight_delta: ' + str(weight_delta))
