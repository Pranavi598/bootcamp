import sys

# Print the Python path to ensure the module directories are included
print("Current Python Path:")
print(sys.path)

# Optionally, check if the utils directory is in the Python path
print("\nChecking if 'utils' directory is in the Python path:")
if 'utils' in sys.path:
    print("Found 'utils' directory in the path.")
else:
    print("Could not find 'utils' directory in the path.")
