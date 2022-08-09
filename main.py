from calculator_mlotfic import calculator

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
        cal = calculator.Calculator(x, y)
        
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