import math
import time
def fact():
    while True:
        user_input = input("Enter the number whose factorial you want to get OR type 'end' to stop the program:  ")
        if user_input == "end":
            print("Program ended.")
            break
        try:
            num = int(user_input)
            Result = math.factorial(num)
            print("Result is being calculated....")
            for i in range(3,0,-1):
                time.sleep(1)
                print(i)
            print(f"The factorial of {num} is {Result}")
        except ValueError:
            print("That's not a number; enter a number or type 'end' to stop the program:  ")
if __name__ == "__main__":
    fact()