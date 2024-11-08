registers = [0] * 32

def ex(instruction):
    parts = instruction.split()
    opcode = parts[0]

    if opcode == "MOV":
        dst, src = parts[1], parts[2]
        registers[int(dst[1:])] = registers[int(src[1:])]
    elif opcode == "ADD":
        dst, src0, src1 = map(int, map(lambda x: x[1:], parts[1:]))
        registers[dst] = registers[src0] + registers[src1]
    elif opcode == "SUB":
        dst, src0, src1 = map(int, map(lambda x: x[1:], parts[1:]))
        registers[dst] = registers[src0] - registers[src1]
    elif opcode == "MUL":
        dst, src0, src1 = map(int, map(lambda x: x[1:], parts[1:]))
        registers[dst] = registers[src0] * registers[src1]
    elif opcode == "DIV":
        dst, src0, src1 = map(int, map(lambda x: x[1:], parts[1:]))
        if registers[src1] != 0:
            registers[dst] = registers[src0] // registers[src1]
        else:
            # 处理除0情况
            print("Error: Division by zero")
    elif opcode == "PRINT":
        dst = int(parts[1][1:])
        print(registers)
        print(registers[dst])

# 读取指令并执行
if __name__ == "__main__":
    instructions = []

    while True:
        try:
            ex(input())
        except EOFError:
            break
