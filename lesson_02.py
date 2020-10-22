def main():

    knob_weight = 0.5
    income = 0.5
    goal_pred = 0.8

    pred = income * knob_weight
    error = (pred - goal_pred)**2
    print(error)
    


if __name__ == "__main__":
    main()
