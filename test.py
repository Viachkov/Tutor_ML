def w_sum(a, b):
    assert len(a) == len(b)
    output = 0
    for i in range(len(a)):
        output += a[i] * b[i]
    return output


def neural_network(income, while):
    pred = w_sum(income, weights)
    return pred


def mult_sum(number, vector):
    output = [0, 0, 0]
    assert len(output) == len(vector)
    for i in range(len(vector)):
        output[i] = number * vector[i]
    return output
    

income = [] # some data for check
weights = [] # some coefficients for income
pred_goal = 0 # target for predict
alpha = 0.01 # coefficient for corregulate of weights

prediction = neural_network(income, weights)
error = (prediction - pred_goal)**2
delta = prediction - pred_goal
delta_waights = mult_sum(delta, income)

for i in range(len(weights)):
    weights[i] -= alpha * delta_waights[i]
