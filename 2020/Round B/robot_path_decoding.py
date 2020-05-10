from collections import deque

BILLION = 1000000000

command_actions = {
    'N': lambda x,y: [x, (y-1) % BILLION],
    'S': lambda x,y: [x, (y+1) % BILLION],
    'W': lambda x,y: [(x-1) % BILLION, y],
    'E': lambda x,y: [(x+1) % BILLION, y]
}

def robot_path_decoding():
    program_code = input()

    positions_stack = deque()
    multipliers_stack = deque()

    position = [0, 0]
    multiplier = 1

    for i in range(len(program_code)):
        command = program_code[i]

        if command.isalpha():
            position = command_actions[command](position[0], position[1])

        elif command.isdigit():
            positions_stack.append(position)
            multipliers_stack.append(multiplier)

            position = [0, 0]
            multiplier = int(command)

        elif command == ')':
            projected_position = [
                (position[0] * multiplier) % BILLION,
                (position[1] * multiplier) % BILLION
            ]

            last_position = positions_stack.pop()

            position = [
                (last_position[0] + projected_position[0]) % BILLION,
                (last_position[1] + projected_position[1]) % BILLION
            ]

            multiplier = multipliers_stack.pop()
    
    position[0] = (position[0] % BILLION) + 1
    position[1] = (position[1] % BILLION) + 1

    return position

# --- Initial point --- #        
test_cases = int(input())

for t in range(test_cases):
    final_position = robot_path_decoding()
    print('Case #{}: {} {}'.format(t+1, final_position[0], final_position[1]))

