import math

def is_perfect_square(num):
    return math.sqrt(num).is_integer() if num >= 0 else False

def perfect_subarray():
    
    n = int(input())
    arr = [int(x) for x in input().split()]

    perfect_subarrays = 0

    for i in range(n):

        sum = 0

        for j in range(i, n):
            
            sum += arr[j]

            if is_perfect_square(sum):
                perfect_subarrays += 1

    return perfect_subarrays


# --- Initial point --- #        
test_cases = int(input())

for t in range(test_cases):
    result = perfect_subarray()
    print('Case #{}: {}'.format(t+1, result))
