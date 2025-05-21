def copy_file_line_by_line(source, destination):
    with open(source, 'r') as src, open(destination, 'w') as dest:
        for line in src:
            dest.write(line)

def main():
    source_file = "source.txt"  # Ensure this file exists or change path
    dest_file = "destination.txt"
    copy_file_line_by_line(source_file, dest_file)

if __name__ == "__main__":
    main()
