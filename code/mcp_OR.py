print("OR Gate")

w1 = 1
w2 = 1
threshold = 2

inputs = [(0,0), (0,1), (1,0), (1,1)]

for x1, x2 in inputs:

    net = x1*w1 + x2*w2

    if net >= threshold:
        output = 1
    else:
        output = 0

    print(x1, x2, "Output:", output)