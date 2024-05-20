import numpy as np

# 定义目标函数
def f(x):
    return np.exp(x) + x**2

# 定义目标函数的一阶导数
def f_prime(x):
    return np.exp(x) + 2*x

# 梯度下降算法
def gradient_descent(f, f_prime, x0, learning_rate=0.01, precision=1e-6, max_iters=10000):
    x = x0
    for i in range(max_iters):
        grad = f_prime(x)
        new_x = x - learning_rate * grad
        if abs(new_x - x) < precision:
            break
        x = new_x
    return x

# 初始猜测值
x0 = 0.0

# 调用梯度下降算法
minimum_x = gradient_descent(f, f_prime, x0)

# 打印结果
print(f"函数在 x = {minimum_x:.8f} 处取得最小值，最小值为 f(x) = {f(minimum_x):.8f}")
