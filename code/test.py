print ("XPR gate")

inputs = [(0,0),(0,1),(1,0),(1,1)]


for x1,x2 in inputs:

    h1_net = x1*1 + x2*(-1)
    if h1_net >= 1:
        h1 = 1
    else:
        h1 = 0
    
    h2_net = x1*(-1) + x2*1
    if h2_net >= 1:
        h2 = 1
    else:
        h2 = 0
    
    final_net = h1*1 + h2*1
    if final_net >= 1:
        output = 1
    else:
        output = 0
    
    print(x1,x2,output)