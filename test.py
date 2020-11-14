import numpy as np

np.random.seed(1)

def relu(x):
    # return x or 0 if x < 0
    return (x > 0) * x

def relu2deriv(output):
    # return 1 if output > 0 or 0
    return output > 0

alpha = 0.2
hidden_size = 4

weight_0_1 = 2 * np.random.random((3, hidden_size)) - 1
weight_0_2 = 2 * np.random.random((hidden_size, 1)) - 1

for iteration in range(60):
    layer_2_error = 0
    for i in range(len(streetlights)):
        layer_0 = streetlights[i: i + 1]
        layer_1  = relu(np.dot(layer_0, weieght_0_1))
        layer_2 = np.dot(layer_1, weight_0_2)

        layer_2_error += np.sum((layer_2 - walk_vs_stop[i: i + 1])**2)
        
        layer_2_delta = layer_2 - walk_vs_stop[i: i + 1]

        """ строка вычисляет разность в слое layer_1 с учетом разности в слое layer_2,
        умножая layer_2-delta соответствующие веса weights_0_2"""
        layer_1_delta = layer_2_delta.dot(weight_1_2.T) * relu2deriv(leyer_1)
        
        weight_0_2 += alpha * layer_1.T.dot(layer_2_delta)
        weight_0_1 += alpha * layer_0.T.cot(layer_1_delta)

        if (iteration % 10 == 9):
            print('Error: ' + str(layer_2_error))
        