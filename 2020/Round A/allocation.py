def allocation():
    n, budget = [int(x) for x in input().split()]
    costs = [int(x) for x in input().split()]

    costs.sort()

    cost_sum = 0
    house_count = 0

    for cost in costs:
        if cost_sum + cost < budget:
            cost_sum += cost
            house_count += 1
        elif cost_sum + cost == budget:
            house_count += 1
            break
    
    return house_count



# --- Initial point --- #        
test_cases = int(input())

for t in range(test_cases):
    result = allocation()
    print('Case #{}: {}'.format(t+1, result))