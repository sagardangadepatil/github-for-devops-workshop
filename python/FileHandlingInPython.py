#It contain 4 types
#1.Open take two parameters path of file with name and mode where 'r' read, 'a' append, 'w' write and 'x' create
#f = open("D:\github-for-devops-workshop\testproject\demo_test.txt", "r")  #Reading file, if file does not exist the it will return with error 
#that case we need to create file using x
c = open("D:/github-for-devops-workshop/python/test.txt", "x")
d = open("test.txt", "r")
print(d.readline())
print(d.readline())
#Need to read only 
e = open("test.txt", "a")
print(e.write('This is my appended First line\n'))
print(e.write('This is my appended Second line\n'))
f = open ("test.txt", "r")
for x in f:
    print(x)
#Close the file using below cmd
f.close()
# During Removal of files using cmds in "FileHandling_removefile.py" file, If it throw an error that means file is open by someone else as well in file name "FileHandlingInPython"
# so before this we need to close file where ever we have open that file i.e in "d" and "e"
c.close()   # Closing "c" file
d.close()   # Closing "d" file
e.close()   # Closing "e" file