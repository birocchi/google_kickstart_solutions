test_cases = int(input())

def calculate_peaks(n, checkpoints):
    total_peaks = 0
    for i in range(1,n-1):
        if checkpoints[i-1] < checkpoints[i] and checkpoints[i] > checkpoints[i+1]:
            total_peaks += 1
    return total_peaks
        

for t in range(test_cases):
    n = int(input())
    checkpoints = [int(cp) for cp in input().split()]

    print('Case #{}: {}'.format(t+1, calculate_peaks(n, checkpoints)))
    
