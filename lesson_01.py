def main():

            #toes #wired #nfans
    ih_wgt = [[0.1, 0.2, -0.1],  #hid[0]
            [-0.1, 0.1, 0.9],    #hid[1]
            [0.1, 0.4, 0.1]]     #hid[2]

            #hid[0] #hid[1] #hid[2]
    hp_wgt = [[0.3, 1.1, -0.3], #damage?
            [0.1, 0.2, 0.0],    #win?
            [0.0, 1.3, 0.1]]    #sorrow?
    weights = [ih_wgt, hp_wgt]

    toes = [8.5, 9.5, 9.9, 9.0]
    vlrec = [0.65, 0.8, 0.8, 0.9]
    nfans = [1.2, 1.3, 0.5, 1.0]
    income = [toes[0], vlrec[0], nfans[0]]


    def w_sum(a, b):
        assert len(a) == len(b)
        output = 0
        for i in range(len(a)):
            output += a[i] * b[i]
        return output

    def vect_mat_mult(vect, matrix):
        output = [0, 0, 0]
        assert len(vect) == len(matrix)
        for i in range(len(matrix)):
            output[i] = w_sum(vect, matrix[i])
        return output

    def neural_nerwork(income, weights):
        hid = vect_mat_mult(income, weights[0])
        pred = vect_mat_mult(hid, weights[1])
        return pred
    prediction = neural_nerwork(income, weights)

    print('Prediction: ', prediction)

    #NumPy version
    import numpy as np
    ih_wgt_np = np.array([[0.1, 0.2, -0.1],
                        [-0.1, 0.1, 0.9],
                        [0.1, 0.4, 0.1]]).T

    hp_wgt_np = np.array([[0.3, 1.1, -0.3],
                        [0.1, 0.2, 0.0],
                        [0.0, 1.3, 0.1]]).T
    weights_np = np.array([ih_wgt_np, hp_wgt_np])

    toes_np = np.array([8.5, 9.5, 9.9, 9.0]) 
    wlrec_np = np.array([0.65, 0.8, 0.8, 0.9])
    nfans_np = np.array([1.2, 1.3, 0.5, 1.0])
    income_np = np.array([toes_np[0], wlrec_np[0], nfans_np[0]])

    def neural_nerwork_np(income_np, weights_np):
        hid_np = income_np.dot(weights_np[0])
        pred_np = hid_np.dot(weights_np[1])
        return pred_np

    prediction_np = neural_nerwork_np(income_np, weights_np)

    print('Prediction_NP: ', prediction_np)


if __name__ == "__main__":
    main()