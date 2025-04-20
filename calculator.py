def calculator():
    while True:
        print("\nSimple Calculator")
        print("Enter 'exit' to quit")
       
        num1 = input("Enter first number: ")
        if num1.lower() == 'exit':
            break
        num2 = input("Enter second number: ")
        if num2.lower() == 'exit':
            break
        operator = input("Enter operator (+, -, *, /): ")
        if operator.lower() == 'exit':
            break
        
        try:
            num1 = float(num1)
            num2 = float(num2)
            
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Error: Division by zero!")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator. Please use +, -, *, or /.")
                continue
            
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input! Please enter numbers only.")