# Using slice function

print('Reversal using Slice function')
# str[start:stop:step]
trial='reversal'
new_trial=trial[::-1]
print(new_trial)


# Recursion
print('Reversal using Recursion')
def string_reverse(str):
    if len(str)==0:
        return str
    else:
        return string_reverse(str[1:])+str[0]
    
str='reversal'
reversed=string_reverse(str)
print(reversed)