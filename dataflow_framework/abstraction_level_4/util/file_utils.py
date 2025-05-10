# abstraction_level_4/utils/file_utils.py
def read_input(input_file):
    with open(input_file, 'r') as file:
        return file.readlines()

def write_output(output_file, lines):
    with open(output_file, 'w') as file:
        file.writelines(lines)

