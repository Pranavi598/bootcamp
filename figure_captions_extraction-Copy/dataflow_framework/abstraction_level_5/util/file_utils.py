def read_lines(file_path):
    with open(file_path, 'r') as f:
        return [line.rstrip('\n') for line in f]
