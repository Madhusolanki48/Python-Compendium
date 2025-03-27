def divide_by(a,b):
    return a/b

try:
    ans=divide_by(40,0)
# except Exception as e:
except ZeroDivisionError as e:
    # print("Something went Wrong !",e)
    # print(e,__class__)
    print(e,"We cannot divide by zero")
except Exception as e:
    print(e,"Something went Wrong !")


# print(divide_by(40,0))

# IndexError

items = [1,2,3,4,5]
item = items[6]
print(item)
try:
    item=items[6]
    print(item)
except:
    print("The index does not exist in the list.")

# ZeroDivisionError
def divide_by(a, b):
    try:
       return a / b
    except ZeroDivisionError:
       return 0
    except Exception as e:
        print(e,'Something went Wrong!')
ans = divide_by(40, 0)
print(ans)


# FileNotFoundError
try :
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except:
    print("Unable to locate file")