command_dict = {
    'N': lambda x,y: [x, y-1],
    'S': lambda x,y: [x, y+1],
    'W': lambda x,y: [x-1, y],
    'E': lambda x,y: [x+1, y]
}

def handle_alpha(alpha, position, i):
    new_position = command_dict[alpha](position[0], position[1])
    position[0] = new_position[0]
    position[1] = new_position[1]
    return i + 1

def handle_digit(digit, program_code, position, i):
    original_position = [position[0], position[1]]
    i_resulted = path_decoding(program_code, position, i+1)

    delta_x = position[0] - original_position[0]
    delta_y = position[1] - original_position[1]
    
    position[0] = (original_position[0] + delta_x * digit) % 1000000000
    position[1] = (original_position[1] + delta_y * digit) % 1000000000

    return i_resulted

def path_decoding(program_code, position, i):
    while i < len(program_code):
        command = program_code[i]

        if command.isalpha():
            i = handle_alpha(command, position, i)
        elif command.isdigit():
            i = handle_digit(int(command), program_code, position, i)
        elif command == '(':
            i += 1
        elif command == ')':
            i += 1
            break

    return i

def robot_path_decoding():
    program_code = input()

    position = [0, 0]
    i = 0

    path_decoding(program_code, position, i)

    # Normalize the final response into the challenge output format
    final_position = [
        (position[0] % 1000000000) + 1, 
        (position[1] % 1000000000) + 1
    ]
    
    return final_position

# --- Initial point --- #        
test_cases = int(input())

for t in range(test_cases):
    final_position = robot_path_decoding()
    print('Case #{}: {} {}'.format(t+1, final_position[0], final_position[1]))

