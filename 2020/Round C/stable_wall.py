def is_wall_stable(wall, rows, columns):

    for c in range(columns):

        found_polys = set()
        current_poly = ''

        for r in reversed(range(rows)):

            poly = wall[r][c]

            if poly not in found_polys:
                found_polys.add(poly)
                current_poly = poly
                continue

            if poly == current_poly:
                continue
            
            return False

    return True

def stable_wall():
    
    rows, columns = [int(x) for x in input().split()]
    wall = [input() for r in range(rows)]

    polys_order = ''

    if not is_wall_stable(wall, rows, columns):
        return ''

    polys_order = 'ZOMA'

    return polys_order

# --- Initial point --- #        
test_cases = int(input())

for t in range(test_cases):
    result = stable_wall()
    print('Case #{}: {}'.format(t+1, result if result else -1))
