from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit return.")

input("?")

print("Opening the file...")
# a creates a new file if not already existed, cursor placed at the end of the text when opened, when use a+ to read, reads nothing because starts from end of file. 
# r read start from begining fo file.
# w creates a new file if not already existed, cursor placed at the begining of the text when opened, overwrite the file. 
target = open(filename, 'r+')

print("Truncating the file. Goodbye!")
# target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

'''
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
'''

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print("And finally, we close it.")
target.close()