def relu(x):
    return (x > 0) * x


num_pos  = relu(2)
num_neg = relu(-2)
num_zero = relu(0)

print(num_pos)
print(num_neg)
print(num_zero)

