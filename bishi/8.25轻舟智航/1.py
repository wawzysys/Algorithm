import math

# 计算角度
def get_angle(x1, y1, x2, y2, x3, y3):
    v1_x = x1 - x2
    v1_y = y1 - y2
    v2_x = x3 - x2
    v2_y = y3 - y2

    dot_product = v1_x * v2_x + v1_y * v2_y
    magnitude_v1 = math.sqrt(v1_x**2 + v1_y**2)
    magnitude_v2 = math.sqrt(v2_x**2 + v2_y**2)

    cos_theta = dot_product / (magnitude_v1 * magnitude_v2)
    angle = math.acos(cos_theta) * (180 / math.pi)
    
    return angle

def main():
    n = int(input("请输入顶点数："))
    angle_sum = (n - 2) * 180  # 凸多边形的总内角和

    arr_x = []
    arr_y = []

    # 读入顶点坐标
    for _ in range(n):
        x, y = map(int, input().split())
        arr_x.append(x)
        arr_y.append(y)

    sum_angles = 0  # 实际的内角和

    # 读入各角
    for i in range(n):
        if i == 0:
            angle = get_angle(arr_x[-1], arr_y[-1], arr_x[i], arr_y[i], arr_x[i + 1], arr_y[i + 1])
        elif i == n - 1:
            angle = get_angle(arr_x[i - 1], arr_y[i - 1], arr_x[i], arr_y[i], arr_x[0], arr_y[0])
        else:
            angle = get_angle(arr_x[i - 1], arr_y[i - 1], arr_x[i], arr_y[i], arr_x[i + 1], arr_y[i + 1])
        
        sum_angles += angle

    # 判断是否为凸多边形
    if sum_angles < angle_sum:
        print("这不是凸多边形")
    else:
        print("这是凸多边形")

if __name__ == "__main__":
    main()
