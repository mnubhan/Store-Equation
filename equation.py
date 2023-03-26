# This program is used to calculate the result of two numbers and write the result to a file equation.txt
# It will ask the user to enter the first number, second number and the arithmatic operation
# It will use exeception heandling to handle errors by using try and except
# Try block of code will run the code and catch any errors
# Except block of code will run if there is an error/exception object is raised
try:
    print(
        "---------------------------------------"
        "\nWelcome equation program."
        "\nBefore start the program did you want to read the equation file or start the program?"
    )
    choose_answer=input(
        "Please enter 'read' to read the file or 'start' to start the program: "
    )
    if choose_answer == "read":
        file_name=input("Please enter the file: ")
        file = open(file_name, "r")
        print(file.read())
    else:
        num1 = int(input("Please enter the first number: "))
        num2 = int(input("Please enter the second number: "))
        arithmatic_operation = input("Please enter the arithmatic operation: ")
        match arithmatic_operation:
            case "+":
                result = num1 + num2
                operator = "+"
            case "-":
                result = num1 - num2
                operator = "-"
            case "*":
                result = num1 * num2
                operator = "*"
            case "/":
                result = num1 / num2
                operator = "/"
            case default:
                print("Invalid operation please enter one of the following: +, -, *, /")
        print(f"The answer for equation {num1}{operator}{num2} is {result}")
        # below line of code is used to open file in append mode
        # open(path_to_file, mode)
        # mode = "a" means to appends the text file
        # resourse: https://www.javatpoint.com/how-to-write-in-text-file-using-python#:~:text=The%20write()%20function%20is,the%20set%20of%20strings%2C%20etc.
        # file = open("equation.txt", "w")
        file = open("equation.txt", "a")
        file.write(f"{num1}{operator}{num2}={result}")
        file.write("\n")
except ValueError:
    print("Invalid input please enter a number")
except ZeroDivisionError:
    print("Cannot divide by zero")
except FileNotFoundError:
    file_name=input("Please enter the correct file name: ")
    file_name = open(file_name, "r")
