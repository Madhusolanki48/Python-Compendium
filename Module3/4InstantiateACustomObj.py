class Recipe():
    # def __new__(cls:type[Self])->Self:
    #     pass

    # def __init__(self)->None:
    #     pass

    def __init__(self,dish,items,time)->None:
        self.dish=dish
        self.items=items
        self.time=time

    def contents(self):
        print('The '+self.dish+' has '+ str(self.items) +\
              ' and takes '+ str(self.time)+' min to prepare')
        
pizza=Recipe('Pizza',['cheese','bread','tomato'],45)
pasta=Recipe('Pasta',['penne','sauce'],55)

print(pizza.items)
print(pasta.items)

print(pizza.contents())

# EXERCISE
'''Step1. 1.1 Define a class called MyFirstClass.
          1.2 Add a print statement inside it such as “Who wrote this?”.

   Step2. Create a string variable named index and initialize it with a string “Author-Book”.

   Step3. 3.1 Define a function called hand_list() with the help of def keyword. 
          3.2 Pass the parameter  self to it. And then pass two parameters, philosopher and book to it.

   Step4. 4.1 Write a print statement using the print() function and pass the class variable by accessing it. 
        Hint: Class variables are accessed directly by calling it over the class name using dot notation.
          4.2 Write a print statement that will give output such as: “Plato wrote the book: Republic” where “Plato” is the philosopher and “Republic” is the book. 
        Hint: You can make use of the built-in (+) concatenation operator to join these strings.

   Step5. 5.1 Create and instantiate an object of that class, called whodunnit
          5.2 Call method hand_list() over this object “whodunnit” and pass two values to it namely “Sun Tzu” and “The Art of War”.
          '''

class MyFirstClass():
    index='Author-Book'

    def __init__(self):
        print('Who wrote this?')# Move the print statement into the constructor

    def hand_list(self,philosopher,book):
        print(MyFirstClass.index)
        print(philosopher+' wrote the book' +book)

whodunnit=MyFirstClass()
whodunnit.hand_list('Sun Tzu','The Art of War')


# The method call prints the output again because the class body is evaluated once more when the class instance is created.
#To avoid this behavior, move the print("Who wrote this?") statement into the constructor (__init__) of the class, so that it runs only once when the class is instantiated.    
