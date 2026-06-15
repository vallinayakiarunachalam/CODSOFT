def calculator():
    print("\n=== SIMPLE CALCULATOR ===")
    while True:
        try:
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))
            print("\nChoose Operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            print("5.Exit Project")
            choice = input("Enter your choice (1-5):")
            if choice == "1":
                result = n1 + n2
                print(f"Result = {result}")
            elif choice == "2":
                result = n1 - n2
                print(f"Result = {result}")
            elif choice == "3":
                result = n1 * n2
                print(f"Result = {result}")
            elif choice == "4":
                if n2 == 0:
                    print("Error: Cannot divide by zero!")
                else:
                    result = n1/n2
                    print(f"Result = {result}")
            elif choice == "5":
                print("Existing calculator. Goodbye!")
                break
            else:
                print("Invalid choice! Please run the program again.")
        except ValueError:
            #Thos fixes your syntax error by handling non-numeric inputs safely!
            print("Error: Please enter valid numbers only.")
calculator()
