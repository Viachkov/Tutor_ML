weight = [0.1, 0.2, 0]
toes = [8.5, 9.5, 9.9, 9.0]
werc = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]
income = werc[0]

def ele_mult(number, vector):
    output =[0, 0, 0]
    assert len(output) == len(vector)
    for i in range(len(vector)):
        output[i] = number * vector[i]
    return output

def neural_network(income, weight):
    pred = ele_mult(income, weight)
    return pred

prediction = neural_network(income, weight)
print("Predicion ", prediction)
