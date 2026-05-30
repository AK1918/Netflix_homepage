print("Perceptron Learning Algorithm")

x = [
    [0,0],
    [0,1],
    [1,0],
    [1,1]
]

y = [0,0,0,1]

w1 = 0
w2 = 0
b = 0

learning_rate = 0.1

for epoch in range(10):

    for i in range(len(x)):

        net = x[i][0]*w1 + x[i][1]*w2 + b

        if net >= 0:
            output = 1
        else:
            output = 0

        error = y[i] - output

        w1 = w1 + learning_rate * error * x[i][0]
        w2 = w2 + learning_rate * error * x[i][1]

        b = b + learning_rate * error

print("Final Weights:")
print("w1 =", w1)
print("w2 =", w2)
print("bias =", b)

print("\nTesting")

for i in range(len(x)):

    net = x[i][0]*w1 + x[i][1]*w2 + b

    if net >= 0:
        output = 1
    else:
        output = 0

    print(x[i], "Output:", output)