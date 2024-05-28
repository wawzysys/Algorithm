import numpy as np
def bilateral_filter(image):
    n = len(image)
    output_image = np.zeros((n, n), dtype=int)
    def compute_weight(i, j, p_center, p_neighbor):
        return 512 - (128 * i**2 + 128 * j**2 + abs(p_neighbor - p_center))
    for x in range(n):
        for y in range(n):
            weighted_sum = 0
            total_weight = 0
            for i in range(-1, 1 + 1):
                for j in range(-1, 1 + 1):
                    if 0 <= x + i < n and 0 <= y + j < n:
                        weight = compute_weight(i, j, image[x, y], image[x + i, y + j])
                        weighted_sum += weight * image[x + i, y + j]
                        total_weight += weight
            
            if total_weight != 0:
                output_value = weighted_sum / total_weight
            else:
                output_value = image[x, y]
            output_image[x, y] = min(max(int(round(output_value)), 0), 255)
    return output_image

n = int(input())

input_data = [list(map(int, input().split())) for _ in range(n)]
filtered_image = bilateral_filter(np.array(input_data))

for row in filtered_image:
    for pixel in row:
        print(pixel)
