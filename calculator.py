"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
from arithmetic import *
import decimal

def main():

    while True:
        input = raw_input(">")
        tokens = input.split(" ")

        if tokens[0] == 'q':
            break

        if tokens[0] not in ["cube", "square", "power", "mod"]:
            if tokens[0].isalpha() or tokens[1].isalpha() or tokens[2].isalpha():
                print "That's not a valid input. Please try again!"



        else:
            num1 = decimal.Decimal(tokens[1])

            if tokens[0] != "cube" and tokens[0] != "square" and tokens[0] != "q":
                num2 = decimal.Decimal(tokens[2])

            if tokens[0] == "+":
                print add(num1, num2)

            if tokens[0] == "-":
                print subtract(num1, num2)

            if tokens[0] == "*":
                print multiply(num1, num2)

            if tokens[0] == "/":
                print divide(num1, num2)

            if tokens[0] == "cube":
                print cube(num1)

            if tokens[0] == "square":
                print square(num1)

            if tokens[0] == "power":
                print power(num1, num2)

            if tokens[0] == "mod":
                print mod(num1, num2)






if __name__ == '__main__':
    main()
