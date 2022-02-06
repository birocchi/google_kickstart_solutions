def transform(padlock, favorites):
    final_sum = 0

    for c in padlock:
        diffs = [min((ord(c) - ord(x)) % 26, (ord(x) - ord(c)) % 26) for x in favorites]
        min_diff = min(diffs)
        final_sum += min_diff

    return final_sum


t = int(input())

for i in range(1, t+1):
    S = input()
    F = input()
    result = transform(S, F)
    print(f'Case #{i}: {result}')
