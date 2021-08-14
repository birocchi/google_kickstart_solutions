from collections import Counter


def integer_mean(a, b):
    summ = a + b
    if summ % 2 == 0:
        return summ // 2
    return None

def check_arithmetic_progression(num1, num2, num3):
    # Three numbers are an arithmetic progression if the middle one is the mean of the other two
    if integer_mean(num1, num3) == num2:
        return 1
    return 0

def calculate_best_center(grid):
    means = []
    
    # Middle row and column
    means.append(integer_mean(grid[1][0], grid[1][2]))
    means.append(integer_mean(grid[0][1], grid[2][1]))

    # Descending and ascending diagonals
    means.append(integer_mean(grid[0][0], grid[2][2]))
    means.append(integer_mean(grid[2][0], grid[0][2]))

    count = Counter(means)

    if None in count:
        count.pop(None)
    
    if len(count):
        # Get the mean that occured most times, maximizing the number of possible arithmetic progressions
        return count.most_common(1)[0][0]
    
    return grid[1][1]

def calculate_arithmetic_square(grid):
    grid[1][1] = calculate_best_center(grid)
    
    progressions_count = 0

    # Upper and lower rows
    progressions_count += check_arithmetic_progression(grid[0][0], grid[0][1], grid[0][2])
    progressions_count += check_arithmetic_progression(grid[2][0], grid[2][1], grid[2][2])

    # Left and right columns
    progressions_count += check_arithmetic_progression(grid[0][0], grid[1][0], grid[2][0])
    progressions_count += check_arithmetic_progression(grid[0][2], grid[1][2], grid[2][2])

    # Middle row and column
    progressions_count += check_arithmetic_progression(grid[1][0], grid[1][1], grid[1][2])
    progressions_count += check_arithmetic_progression(grid[0][1], grid[1][1], grid[2][1])

    # Descending and ascending diagonals
    progressions_count += check_arithmetic_progression(grid[0][0], grid[1][1], grid[2][2])
    progressions_count += check_arithmetic_progression(grid[2][0], grid[1][1], grid[0][2])
    
    return progressions_count


t = int(input())

for i in range(t):
    grid = []

    for _ in range(3):
        grid.append(list(map(int, input().split())))
    
    # Include in the grid the missing center number
    grid[1].insert(1, 0)
    
    print(f'Case #{i+1}: {calculate_arithmetic_square(grid)}')
