# Algorithm for a Palindrome

str='racecar'

print(str[0])
print(str[6])

# [0]==[6]
# [1]==[5]
# [2]==[4]

def isPalindrome(str):
    startIndex=0
    endIndex=len(str)-1

    for x in str:
        if str[startIndex] != str[endIndex]:
            return False
        return True
    
print(isPalindrome('racecar'))