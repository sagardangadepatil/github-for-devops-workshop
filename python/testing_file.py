# Open a file in write mode (this will create the file if it doesn't exist)
with open("example.txt", "w") as file:
    file.write("Hello, this is a test!\n")
    file.write("Writing another line to the file.")
