import numpy as np

weights = np.array([])
alpha = 0.1

streetlights = np.array([[],])
walk_vs_stop = np.array([])

income = streetlights[0]
goal_predict = walk_vs_stop[0]

for iter in range(40):
    error_all_lights = 0
    for raw_index in range(len(walk_vs_stop)):
        income = streetlights[raw_index]
        goal_predict = walk_vs_stop[raw_index]
        prediction = income.dot(weights)
        error = (prediction - goal_predict)**2
        error_all_lights += error
        delta = prediction - goal_predict
        weights -= alpha * (income * delta)
        print('Prediction ', prediction)
    print('Errors of all lights: ', error_all_lights)
