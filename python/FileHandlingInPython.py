#It contain 4 types
#1.Open take two parameters path of file with name and mode where 'r' read, 'a' append, 'w' write and 'x' create
#f = open("D:\github-for-devops-workshop\testproject\demo_test.txt", "r")  #Reading file, if file does not exist the it will return with error
d = open ("D:/github-for-devops-workshop/python/list.py", "r")
print(d.read())