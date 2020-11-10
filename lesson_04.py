import numpy as np

def main():
    np.random.seed(1)

    def relu(x):
        """ change negative figures into zero"""
        return (x > 0) * x

    alpha = 0.2
    hidden_size = 4

    streetlights = np.array([[1, 0, 1],
                            [0, 1, 1],
                            [0, 0, 1],
                            [1, 1, 1]])

    walk_vs_stop = np.array([1, 1, 0, 1]).T

    weights_0_1 = 2 * np.random.random((3, hidden_size)) - 1        # Change negative figures into zero
    weights_0_2 = 2 * np.random.random((hidden_size, 1)) - 1        # Change negative figures into zero

    layer_0 = streetlights[0]
    layer_1 = relu(np.dot(layer_0, weights_0_1))
    layer_2 = np.dot(layer_1, weights_0_2)

    print('Weights_0_1: ', weights_0_1)
    print('Weights_0_2: ', weights_0_2)
    print('Layer_0: ', layer_0)
    print('Leyer_1: ', layer_1)
    print('Leyer_2: ', layer_2)


if __name__ == "__main__":
    main()
