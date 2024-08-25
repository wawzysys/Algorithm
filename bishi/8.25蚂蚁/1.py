import numpy as np
from sklearn.svm import SVC
def solve(data):
    data = np.array(data, dtype=float)
    X = data[:, :-1]
    y = data[:, -1]

    model = SVC(kernel='linear', C=1e5)  
    model.fit(X, y)

    nums = np.abs(model.dual_coef_[0])

    output = [f"{x:.2f}" if x != 0 else "0.00" for x in nums]
    return output

data = []
while True:
    try:
        line = input().strip()
        if not line:
            break
        data.append(list(map(float, line.split())))
    except EOFError:
        break

nums = solve(data)
print(nums)
