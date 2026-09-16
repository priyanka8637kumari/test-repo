# Create a new file and print a message
file_name = "new_file2.txt"

with open(file_name, "w", encoding="utf-8") as file:
    file.write("This is a newly created file.\n")

print(f"New file created: {file_name}")
