# Remove files using below cmds If it throw an error that means file is open by someone else as well in file name "FileHandlingInPython"
# so before this we need to close file where ever we have open that file i.e in "d" and "e"
import os
print(os.remove("D:/github-for-devops-workshop/python/test.txt"))