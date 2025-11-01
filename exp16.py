

import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def feedforward(x1, x2, w1, w2, b):
    z = x1*w1[0] + x2*w1[1] + b[0]
    h1 = sigmoid(z)
    z2 = x1*w2[0] + x2*w2[1] + b[1]
    h2 = sigmoid(z2)
    output = sigmoid(h1*1.5 + h2*1.5 + b[2])
    return output

print("Simple Feedforward Neural Network for XOR")

for x1, x2 in [(0,0), (0,1), (1,0), (1,1)]:
    out = feedforward(x1, x2, [0.5, 0.6], [0.7, 0.8], [0.1, 0.2, 0.3])
    print(f"Input: {x1},{x2} => Output: {round(out, 3)}")
