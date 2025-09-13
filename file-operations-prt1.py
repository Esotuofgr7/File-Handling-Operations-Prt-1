# Write in File using with()function
with open('sandy.txt', 'w') as file:
    file.write("Hi! I am Penguin an di am 1 yr old.")
file.close()

with open('destroyed.txt', 'r') as file:
    data = file.readlines()
    print("Words in this file are....")
    for line in data:
        word = line.split()
        print (word)
file.close()