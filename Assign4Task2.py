# Task 2: Write and Append Data to a File

# Step 1: Write user input to the file
write_data = input("Write to the file: ")
with open("output.txt", "w") as file:
    file.write(write_data + "\n")
print("Data successfully written to output.txt.")

# Step 2: Append additional data to the file
append_data = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(append_data + "\n")
print("Data successfully appended.")

# Step 3: Read and display the final content of the file
print("Final content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)
