def f(x):
	return 1 + 5 * x + x ** 3 
print(f(1))
print(f((f(1) + 1)))
# (n + 1) ^ 3 = n ^ 3 + 3 * n ^ 2 + 3 * n + 1
# (n + 1) ^ 4 = n ^ 4 + 4 * n ^ 3 + 6 * n ^ 2 + 4 * n + 1