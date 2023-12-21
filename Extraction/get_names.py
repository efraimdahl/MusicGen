import os
import sys

if len(sys.argv) < 2:
    print("Please provide the folder path as an argument.")
    sys.exit(1)

folder_path = sys.argv[1]
output_file = 'midi-names.txt'

# Get all filenames with .mid extension in the folder
file_names = [f for f in os.listdir(folder_path) if f.endswith('.mid')]

# Save filenames to a text file
with open(output_file, 'w') as file:
    file.write('\n'.join(file_names))

print(f"All MIDI filenames extracted from '{folder_path}' and saved to '{output_file}' successfully.")
