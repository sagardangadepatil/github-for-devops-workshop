#It contain 4 types
#1.Open take two parameters path of file with name and mode where 'r' read, 'a' append, 'w' write and 'x' create
#f = open("D:\github-for-devops-workshop\testproject\demo_test.txt", "r")  #Reading file, if file does not exist the it will return with error 
#that case we need to create file using x

d = open("test.txt", "r")
print(d.readline())
print(d.readline())
#Need to read only 
e = open("test.txt", "a")
print(e.write('This is my appended First line\n'))
f = open ("test.txt", "r")
for x in f:
    print(x)
#print(g.readline())
#g = open ("D:/github-for-devops-workshop/python/test.txt", "r")
#print(g.read()) 