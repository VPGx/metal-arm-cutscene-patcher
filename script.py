import sys
import hashlib
from colorama import init, Fore

def calculate_md5(file_path):
    with open(file_path, "rb") as file:
        md5_hash = hashlib.md5()
        for chunk in iter(lambda: file.read(4096), b""):
            md5_hash.update(chunk)
        return md5_hash.hexdigest()

# Initialize Colorama for colored output
init()

if len(sys.argv) < 2:
    print("Please drag and drop the .xbe file onto the script.")
    sys.exit(1)

input_xbe = sys.argv[1]

if len(sys.argv) > 2:
    output_file_path = sys.argv[2]
else:
    output_file_path = "cutscene_skip.xbe"

expected_hash = "087c7ce535d7d8f59b29cd8d7b3b0e91"  # XBOX - NTSC - RETAIL

# Calculate the MD5 hash of the input file
md5_hash = calculate_md5(input_xbe)

if md5_hash != expected_hash:
    print(Fore.RED + "Invalid file! The MD5 hash does not match." + Fore.RESET)
    print("Please check your file and try again.")
    sys.exit(1)

# Print the success message in green text
print(Fore.GREEN + "Input XBE Hash Matches!" + Fore.RESET)

with open(input_xbe, "rb") as input_file, open(output_file_path, "wb") as output_file:
    offset = 0x1d20c9
    bytes_to_write = b'\x90\x90'

    # Copy the input file to the output file
    output_file.write(input_file.read())

    # Seek to the desired offset and write the modified bytes
    output_file.seek(offset)
    output_file.write(bytes_to_write)

print(f"Modified file saved as {output_file_path}")
