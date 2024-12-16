def find_min_distance_point(coordinates):

    if not coordinates:
        raise ValueError("坐标列表不能为空。")

    sorted_coords = sorted(coordinates)
    n = len(sorted_coords)
    median = sorted_coords[n // 2] if n % 2 == 1 else sorted_coords[(n // 2) - 1]

    return median


if __name__ == "__main__":
    points = [1, 2, 3, 4, 5]
    print(find_min_distance_point(points)) 
