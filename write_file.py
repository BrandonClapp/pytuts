text = "This is some text\n"

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist but does not overwrite an existing file.
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

file = open("file.txt", "a")  # Append mode
for each in range(10):
    file.write(text)

file.close()
