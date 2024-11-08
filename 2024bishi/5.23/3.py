import numpy as np

def bit_count_activation(z):
    abs_z = abs(z)
    bit_count = bin(abs_z).count('1')
    return 1 if bit_count % 2 != 0 else 0

def single_layer_nn(M, N, x, W1, b1, W2):
    x = np.array(x, dtype=int)
    W1 = np.array(W1, dtype=int).reshape(N, M)
    b1 = np.array(b1, dtype=int)
    W2 = np.array(W2, dtype=int)
    hidden_layer_input = W1.dot(x) + b1
    hidden_layer_output = np.array([bit_count_activation(z) for z in hidden_layer_input])
    y = W2.dot(hidden_layer_output)
    
    return y

M, N = map(int, input().split())
x = [int(input())]
W1 = [int(input())]
b1 = [int(input())]
W2 = [int(input())]

y = single_layer_nn(M, N, x, W1, b1, W2)
print(y)  # 输出: -1
