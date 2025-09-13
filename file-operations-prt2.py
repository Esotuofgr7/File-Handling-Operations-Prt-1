# Create a new file
new_file = open('New_File.txt', 'x')
new_file.close()

# Check if a File exists
import os
print("Checking if my_file exists or not....")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The File does not exist")

# Create a new file if it doesn't
my_file = open("my_file.txt", "w")
my_file.write("Hi! I am Penguin and I am 1 year old.")
my_file.close()

# Delete file named sandy
os.remove('sandy.txt')

# Delete the folder
os.rmdir('DisFolderFiles')