def simple_calculator():
    print("Simple Calculator")
    print("Operations available:")
    print("1.Addition(+)")
    print("2.Subtraction(-)")
    print("3.Multiplication(*)")
    print("4.Division(/)")
    print("5.Modulus(%)")
    print("6.Exponential(**)")
    print()
    num1_input=input("Enter the first number: ")
    num2_input=input("Enter the second number: ")
    if not num1_input.replace('.','',1).isdigit() or not num2_input.replace('.','',1).isdigit():
        print("\nError:Please enter valid numbers:")
        return
    num1=float(num1_input)
    num2=float(num2_input)
    operation=input("Enter the operation (+,-,*,/,%,**):").strip()
    result=None
    operation_name=""
    if operation=='+':
        result=num1+num2
        operation_name="Addition"
    elif operation=='-':
        result=num1-num2
        operation_name="Subtraction"
    elif operation=='*':
        result=num1*num2
        operation_name="Multiplication"
    elif operation=='/':
        if num2==0:
            print("\nError:Division by zero is not allowed.")
            return
        result=num1/num2
        operatiion_name="Division"
    elif operation=="%":
        result=num1%num2
        operation_name="Modulus"
    elif operation=="**":
        result=num1**num2
        operation_name="Exponentiation"
    else:
        print("\nInvalid Operation")
        return
    print(f"\n{operation_name} Result:{num1}{operation}{num2}={result}")
if __name__=="__main__":
    simple_calculator()
