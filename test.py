import  numpy as np

ih_wgt = np.array([[]]).T
ph_wgt = np.array([[]]).T
weightts = np.array([ih_wgt, ph_wgt])

tgame = np.array([])
twins = np.array([])
tfans = np.array([])

income = np.array([tgame[0], twins[0], tfans[0]])

def neural_network(income, weightts):
    hid = income.dot(weightts[0])
    pred = hid.dot(weightts[1])
    return pred

prediction = neural_network(income, weightts)

print('Prediction: ', prediction)
