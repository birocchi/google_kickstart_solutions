def calculate_last_day():
    n, total_days = [int(x) for x in input().split()]
    bus_routes = [int(route) for route in input().split()]
    
    last_possible_day = total_days

    for i in reversed(range(n)):
        last_possible_day = int(last_possible_day/bus_routes[i]) * bus_routes[i]
    
    return last_possible_day

# --- Initial point --- #        
test_cases = int(input())
    
for t in range(test_cases):
    print('Case #{}: {}'.format(t+1, calculate_last_day()))
