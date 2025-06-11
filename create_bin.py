import os

# Get the absolute path to the desktop
desktop_path = os.path.expanduser("~/Desktop")
file_path = os.path.join(desktop_path, "file.bin")

# Print the path
print("Saving to:", file_path)

# Create and write binary data to the file
with open(file_path, "wb") as f:
    f.write(b"\x00\x01\x02\x03\x04")  

print("File created successfully!")
