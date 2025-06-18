#Import the sys module
import sys

# Define a function that takes a paramter "filenames"
def my_cat(filenames):
    # Loop through esach file in the list
    for filename in filenames:
        # Open the current file in read mode "r"
        with open(filename, "r") as file:
         # read the file's content and print it. 'end="" ' prevents adding extra new lines.    
         print(file.read(), end="")
# Call the my_cat function, passing the arguments after the file name [1:], since 0 is the file´s name.
my_cat(sys.argv[1:])