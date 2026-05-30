print("Delta Learning Rule")

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

for i in range(len(x)):

    net = w1*x[i][0] + w2*x[i][1] + b

    error = y[i] - net

    w1 = w1 + learning_rate * error * x[i][0]   
    w2 = w2 + learning_rate * error * x[i][1]
    b = b + learning_rate * error

    print("Weights:", w1, w2)
    print("Bias:", b)