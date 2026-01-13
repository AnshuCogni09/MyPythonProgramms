# Exception Handling:
# It is a process of responding to unwanted or unexpected events that occur during the execution of a program.
# It is handled using try, except, finally blocks in Python.

a = input("Enter number for multiplication: ")

try:
    for i in range(1, 11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except Exception as e:
    print("An error occurred:", e)

# It will print multiplication table if valid number is given.
# if invalid input is given, It will print error message and stop further execution.

# Finally block:
finally:
    print("Execution completed.")
# Finally block will always execute, regardless of whether an exception occurred or not.

# raisin custom exceptions using raise keyword
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        print("You are a minor.")
    else:
        print("You are an adult.")

age = int(input("Enter your age: "))
check_age(age)