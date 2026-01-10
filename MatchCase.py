age = int(input("Enter your age: "))

match age:
    case age if age < 0:
        print("Age cannot be negative.")    
    case age if age < 18:
        print("You are Underage.")
    case age if age >= 18:
        print("You are an Adult.")  