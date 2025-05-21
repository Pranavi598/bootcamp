def run_pipeline(input_file: str, output_file: str, config_file: str):
    with open(input_file, "r") as file:
        lines = file.readlines()

    # Mock transformation
    processed_lines = [line.upper() for line in lines]

    with open(output_file, "w") as outfile:
        outfile.writelines(processed_lines)

    print(f"Processed {input_file} to {output_file}")
