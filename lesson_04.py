import numpy as np

def main():
    weights = np.array([0.5, 0.48, -0.7])
    alpha = 0.1

    streetlights = np.array([[1, 0, 1],
                            [0, 1, 1],
                            [0, 0, 1],
                            [1, 1, 1],
                            [0, 1, 1],
                            [1, 0, 1]])
    
    walk_or_stop = np.array([0, 1, 0, 1, 1, 0])

    income = streetlights[0]
    goal_predict = walk_or_stop[0]

    for iteration in range(40):
        error_for_all_lights = 0
        for row_index in range(len(walk_or_stop)):
            income = streetlights[row_index]
            goal_predict = walk_or_stop[row_index]
            prediction = income.dot(weights)
            error = (prediction - goal_predict)**2
            error_for_all_lights += error

            delta = prediction - goal_predict
            weights -= (alpha * (income * delta))
            print('Prediction: ', prediction)
        print('Error: ', error_for_all_lights)
        print('Weights: ', weights)


if __name__ == "__main__":
    main()
