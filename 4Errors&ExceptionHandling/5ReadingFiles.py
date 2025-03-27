# read(n) --returns the entire content of the file as a string containing all chars
# with open('samplefile.txt','r)as file:'
#     'print(file.read())
    


# readline() --returns a single line as a string
# File Content:
# This is the first line
# This is the second line
# with open(testing.txt','r')as file:'
#     'print(file.readline())'
# output:
# This is the first line


# readlines()--read the entire contents of the file and returns it in an ordered list
# File Content:
# This is the first line
# This is the second line
# This is the third line 
# This is the fourth line
# with open(testing.txt','r')as file:
#     Lines=file.readline())
#     print(len(lines))
#     for line in lines:
#        print(line)
# Output:
# This is the first line
# This is the second line
# This is the third line 
# This is the fourth line


# Absolutte paths:
# /user/local/etc/somefile.txt  or C:\user\system\somefile.txt

# Relative path:
# 'somefile.txt' or './somefile.txt'


with open('4newfile.txt','r')as file:
    print(file.read())

with open('4newfile.txt','r') as file:
    data=file.readlines()
    for x in data:
        print(x)