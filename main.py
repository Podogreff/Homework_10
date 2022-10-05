
with open("myfile.txt", "w") as file:
    file.write("Hello file world!\n")
    file.write("Let's learn Python\n")
# creates a new file named "myfile.txt"

print(open("myfile.txt").read())
# Hello file world!
# Let's learn Python
