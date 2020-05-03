test_cases = int(input())

command_dict = {
    'N': lambda x,y: [x,y-1] if y > 1 else [x,1000000000],
    'S': lambda x,y: [x,y+1] if y < 1000000000 else [x,1],
    'W': lambda x,y: [x-1,y] if x > 1 else [1000000000,y],
    'E': lambda x,y: [x+1,y] if x < 1000000000 else [1,y]
}

def handle_alpha(alpha, position, i):
    new_position = command_dict[alpha](position[0], position[1])
    position[0] = new_position[0]
    position[1] = new_position[1]
    return i+1

def handle_digit(digit, program_code, position, i):
    original_position = [position[0], position[1]]
    j = path_decoding(program_code, position, i+1)

    delta_x = position[0] - original_position[0]
    delta_y = position[1] - original_position[1]
    
    new_x = position[0] + delta_x * (digit-1)
    new_y = position[1] + delta_y * (digit-1)

    new_x_norm = new_x % 1000000000 + int(new_x/1000000000)
    new_y_norm = new_y % 1000000000 + int(new_y/1000000000)

    new_x_norm = new_x_norm if new_x_norm > 0 else 1000000001 + new_x_norm
    new_y_norm = new_y_norm if new_y_norm > 0 else 1000000001 + new_y_norm

    position[0] = new_x_norm
    position[1] = new_y_norm

    return j

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

    position = [1, 1]
    i = 0

    i = path_decoding(program_code, position, i)
    
    return position
        

for t in range(test_cases):
    final_position = robot_path_decoding()
    print('Case #{}: {} {}'.format(t+1, final_position[0], final_position[1]))

