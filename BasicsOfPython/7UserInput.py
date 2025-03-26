num1=input('Please enter a number : ')
num2=input("Please enter another number : ")
print(type(num2))
print(num1+num2)
print(int(num1)+int(num2))


str1=input("Please enter your first name : ")
str2=input("Please enter your second name : ")
print("Hello " +str1+" "+str2)
# Print arguments
# comma separated
print(1,2,3)

# Arithmetic
print(1+3)

# String Concatenation
name='John'
print('Hello '+name)

'''Additional Arguments
oject-ensures values are printed on screen
Sep - how objects being printed or separated
end- defines what gets printed at the end
file- specifies where values get printed to --by defualt(STD out)
flush- boolean exp to flush the buffer moves the data from temp to permanent memory storage 

'''

print('Hello','you!',sep=', ')

# Output Formatting
print("I like {0} more than {1}".format("oranges","grapes"))
