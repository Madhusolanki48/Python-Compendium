menu=['espresso','mocha','latte','cappuccino','cortado','americano']

def find_coffee(coffee):
    if coffee[0]=='c':
        return coffee
   
# map_coffee=map(find_coffee,menu)
# print(map_coffee)
# for x in map_coffee:
#     print(x)

# map takes all objects in a list and applies a function


# Using filter fun

filter_coffee=filter(find_coffee,menu)
print(filter_coffee)
for x in filter_coffee:
    print(x)

# Filter do the same but take the results & create a new list with only the true values
