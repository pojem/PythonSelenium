import functions

#self keyword is mandatory for calling variable names into method
#instance and class variables have whole different purpose
#constructor name should be __init__
#new keyword is not required when you create object

class Calculator:
    num = 100 # class variables
    def __init__(self,a,b):
        print("i am called automatically when object is created")
        self.firstnum = a
        self.secondnum = b

    def getData(self):
        print(" i am now executing as method in class")

    def Summation(self):
        return self.firstnum + self.secondnum + Calculator.num


obj = Calculator(2,3) #first object
print(obj.Summation())
obj1 = Calculator(8,5) #second object
print(obj1.Summation())
