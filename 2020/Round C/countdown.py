def countdown():
    n, k = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]

    num_countdowns = 0
    current_num = k

    for i in range(n):
        
        a = arr[i]

        if a == current_num:
            current_num -= 1
            if current_num == 0:
                num_countdowns += 1
                current_num = k
        else:
            current_num = k
            if a == current_num:
                current_num -= 1

    return num_countdowns

# --- Initial point --- #
test_cases = int(input())

for t in range(test_cases):
    result = countdown()
    print('Case #{}: {}'.format(t+1, result))
