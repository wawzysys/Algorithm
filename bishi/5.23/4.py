import numpy as np

def generate_hamming_codewords():
    G = np.array([
        [1, 0, 0, 0, 1, 0, 1],
        [0, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 1, 1]
    ])
    codewords = []
    for i in range(16):
        b = np.array([int(x) for x in format(i, '04b')])
        codeword = np.dot(b, G) % 2
        codewords.append(codeword)
    return np.array(codewords)

def max_log_map_decode(llr):
    codewords = generate_hamming_codewords()
    llr = np.array(llr)
    
    soft_values = []
    for i in range(4):
        s1 = []
        s0 = []
        for codeword in codewords:
            if codeword[i] == 1:
                s1.append(codeword)
            else:
                s0.append(codeword)
                
        s1 = np.array(s1)
        s0 = np.array(s0)
        
        max_s1 = s1[np.argmax(np.dot(s1, llr))]
        max_s0 = s0[np.argmax(np.dot(s0, llr))]
        
        llr_i = sum([max_s1[j] * llr[j] for j in range(7) if j != i]) - sum([max_s0[j] * llr[j] for j in range(7) if j != i])
        soft_values.append(llr_i)
    
    return soft_values

# 样例输入
llr_input = []
for _ in range(7):
    llr_input.append(float(input()))
decoded_values = max_log_map_decode(llr_input)

# 输出结果
for val in decoded_values:
    print(int(val))
