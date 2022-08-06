# Program make a simple calculator

# class definition
class Calculator():
    '''
    Create a class and using a constructor to initialize values of that class.
    '''
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    # This methos add two nubers
    def add(self):
        return self.x + self.y
    # This methos subtracting two numbers
    def sub(self):
        return self.x - self.y

    # This methos multiplying two numbers
    def mul(self):
        return self.x * self.y  

    # This methos dividing two numbers
    def div(self):
        return self.x / self.y
    

# print the calculator interface
print("Select operation::")
print("0. Exit")
print("1. Add (+) ")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

while True:    
    # take input from the user
    choice = input("Enter choice(0/1/2/3/4): ")
    
    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        x = (input("Enter first number: "))
        y = (input("Enter second number: "))
        
        # creating object from class
        cal = Calculator(x, y)
    
    if choice == '1':
        print("Result: ",cal.add())
    elif choice == '2':
        print("Result: ",cal.sub())
    elif choice == '3':
        print("Result: ",cal.mul())
    elif choice == '4':
        print("Result: ",round(cal.div(),2))
    elif choice == '0':
        print("Exiting!!")
        break
    else:
        print("Invalid Input, please try again")

if __name__ == '__main__':
    cal_obj = Calculator(1, 2)
    print(cal_obj.add())
