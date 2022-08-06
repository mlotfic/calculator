# Simple Calculator Module

Building a python package using simple calculator program 

## In this repo you will git to know :
- How to build a python program into package?
- How tp publish your package to PyPi repo?
- How to create unit test and automate testing for python program?
- How to check for code quailty and styling using pylint on python program?
- How to using GitHub Action :
  1. Publish Python Package 
       - By GitHub Actions
       - Publish a Python Package to PyPI on release.
  2.  Pylint   
        - By GitHub Actions
        - Lint a Python application with pylint.
  3. Python application
      - By GitHub Actions
      - Create and test a Python application.
  4. Python package
      - By GitHub Actions
      - Create and test a Python package on multiple Python versions.

## Program Structure 
### Displaying Interface Options
```py
    # print the calculator interface
    print("Select operation::")
    print("0. Exit")
    print("1. Add (+) ")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
```

### Interaction with users 
```py
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
```

### Class Definition 
```py
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
```

