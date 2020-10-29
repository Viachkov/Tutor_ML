def neural_network(income, weights):
    assert len(income) == len(weights)
    out = 0
    for i in range(len(income)):
        out += income[i] * weights[i]
    return out


def mult_ele(scalar, vector):
    output = [0, 0, 0]
    assert len(output) == len(vector)
    for i in range(len(output)):
        output[i] = scalar * vector[i]
    return output

toes = [8.5, 9.5, 9.9, 9.0]
wlerc = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

income = [toes[0], wlerc[0], nfans[0]]
win_or_lose_binary = [1, 1, 0, 1]
weights = [0.1, 0.2, -0.1]
alpha = 0.01
goal_prediction = win_or_lose_binary[0]
prediction = neural_network(income, weights)

for i in range(3):
    prediction = neural_network(income, weights)

    error = (prediction - goal_prediction)**2
    delta = prediction - goal_prediction
    weights_delta = mult_ele(delta, income)
    # weights_delta[0] = 0

    print('Iterator: ' + str(i + 1))
    print('Prediction: ' + str(prediction))
    print('Delta: ' + str(delta))
    print('Weights: ' + str(weights))
    print('Weights Delta: ' + str(weights_delta))

    for i in range(len(weights)):
        weights[i] = alpha * weights_delta[i]
