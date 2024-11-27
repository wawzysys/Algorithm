# List of 100 integers
numbers = [
    534, 386, 319, 692, 169, 338, 521, 713, 640, 692, 969, 362, 311, 349, 308, 357, 515, 140, 591, 216,
    57, 252, 575, 630, 95, 274, 328, 614, 18, 605, 17, 980, 166, 112, 997, 37, 584, 64, 442, 495,
    821, 459, 453, 597, 187, 734, 827, 950, 679, 78, 769, 661, 452, 983, 356, 217, 394, 342, 697, 878,
    475, 250, 468, 33, 966, 742, 436, 343, 255, 944, 588, 734, 540, 508, 779, 881, 153, 928, 764, 703,
    459, 840, 949, 500, 648, 163, 547, 780, 749, 132, 546, 199, 701, 448, 265, 263, 87, 45, 828, 634
]

def max_sum_divisible_by_24(numbers):
    total_sum = sum(numbers)
    remainder = total_sum % 24

    if remainder == 0:
        return total_sum

    # Find the smallest number with remainder equal to the total_sum % 24
    candidates = [num for num in numbers if num % 24 == remainder]
    if candidates:
        min_candidate = min(candidates)
        return total_sum - min_candidate

    # If no single number can be removed to fix the remainder,
    # try removing two numbers whose remainders add up to the required value
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if (numbers[i] + numbers[j]) % 24 == remainder:
                return total_sum - numbers[i] - numbers[j]

    # If not possible, return 0 (no valid subset)
    return 0

# Calculate and print the maximum sum divisible by 24
print(max_sum_divisible_by_24(numbers))