# Two file handling Functions--Open and close

# OPEN FUNCTION-Reading,writing and creating a file

# open(<FILE_NAME><FILE_LOCATION>,<MODE>) --two args

# Mode sets
# Mode - r (open and read(text format))        Mode - rb (binary format)
# Mode - r+(open for reading and writing)      Mode - w(open for writing)
# Mode a - open(<FILE_NAME>,a) --open file for editing or appending data


# CLOSE FUNCTION -for closing the open file connection
# close()  --don't take any args

# With OPEN FUNCTION
# with open('testing.txt','r) as file:   --no close function needed


file=open('3test.txt', mode='r')
data=file.readline()
print(data)
file.close()

with open('3test.txt', mode= 'r') as file:
 data=file.readline()
 print(data)
