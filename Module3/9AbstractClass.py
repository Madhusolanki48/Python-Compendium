from abc import ABC,abstractmethod   #import ABC & method

class Employee(ABC):                 #define ABC method
     @abstractmethod
     def donate(self):               #create subclass
         pass
     
class Donation(Employee):
    def donate(self):
        a=input('How much would you like to donate: ')
        return a
    
amounts=[]                           #create instances
john=Donation()
j=john.donate()
amounts.append(j)
peter=Donation()
p=peter.donate()
amounts.append(p)

print(amounts)


     