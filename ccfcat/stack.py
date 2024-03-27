def generate_sequences(n):
    def generate(stack, path, result, in_, out):
        if out == n:  # 如果所有元素都已出栈
            result.append(path)
            return
        
        # 如果栈非空，尝试出栈
        if stack:
            generate(stack[:-1], path + [stack[-1]], result, in_, out + 1)
        
        # 如果还有元素可以入栈
        if in_ < n:
            generate(stack + [in_], path, result, in_ + 1, out)
    
    result = []
    generate([], [], result, 0, 0)
    return result

# 生成并存储3个元素的所有出栈顺序
sequences = generate_sequences(3)
for seq in sequences:
    print(seq)
