weight = 0.5
lr = 0.01

toes_of_game = [0.5]
win_or_lost = [1]
income = toes_of_game[0]
true = win_or_lost[0]

def neural_network(income, weight):
    pred = income * weight
    return pred

prediction  = neural_network(income, weight)
error = (true - prediction)**2

print(error)

prediction_up = neural_network(income, weight) + lr
error_up = (true - prediction_up)**2
print(error_up)

prediction_down = neural_network(income, weight) - lr
error_down = (true - prediction_down)**2
print(error_down)

if error > error_up or error > error_down:
    if error_up > error_down:
        weight += lr
        print(weight)
    else:
        weight -= lr
        print(weight)