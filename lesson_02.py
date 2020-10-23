def main():
    weight = 0.1
    lr = 0.01
    def neural_nerwork(income, weight):
        pred = income * weight
        return pred
    
    number_of_toes = [0.5]
    win_lose_binary = [1]
    income = number_of_toes[0]
    true = win_lose_binary[0]

    prediction = neural_nerwork(income, weight)
    error = (prediction - true)**2
    print(error)

    prediction_up = neural_nerwork(income, weight) + lr
    error_up = (true - prediction_up)**2

    prediction_down = neural_nerwork(income, weight) - lr
    error_down = (true - prediction_down)**2

    if error > error_down or error > error_up:
        if error_down > error_up:
            weight += lr
            print('Error_up', error_up)
        else:
            weight += lr
            print('Error_down', error_down)



if __name__ == "__main__":
    main()
