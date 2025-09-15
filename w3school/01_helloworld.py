print("Hello, World!")

# Check the python version of the editor:

import sys
print(sys.version)

# Some more example by using exit()

# Example-1:
age = int(input("Enter Your age: "))
if age < 18:
    print("You are not allowed.")
    exit()
print("Welcome! You can continue")

# Example-2:
name = input("Enter your name: ")
if name.strip() == "":
    print("You must enter a name!")
    exit()
print(f"Hello, {name}!")

# Example-3:
password = input("Enter password: ")
if password != "1234":
    print("Wrong password, exiting..")
    exit()
print("Access granted!")

# Example-4:
for i in range(3):
    code = input("Enter secret code: ")
    if code == "open":
        print("Door unlocked")
        break
else:
    print("Too many failed attempts!")
    exit()
print("You may enter..")

# Example-5:
print("Starting program..")
exit("program stopped due to an unexpected error!")

# Example-6:
for num in range(1, 10):
    if num == 5:
        print("Exiting program at number 5")
        exit()
    print(num)