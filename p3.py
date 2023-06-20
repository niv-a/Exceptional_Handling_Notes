# creating user defined exceptions
# 1. create exception class and inherit it from the base exception class i.e. Exception
#  syntax: class InvalidAge(Exception): pass
# 2. Raise InvalidAge exception for particular condition(age<0) inside try box.bool
#     syntax: try:
#                 if age<0:
#                     raise Invalid("message")
# 3. handle the exception using except block.
# syntax: except Excepton as obj:
#             print(obj)

# -----------------------------------------------------------------
# WAP for SixDivisionError Exception
# -----------------------------------------------------------------

# class FiveDivisionError(Exception):
#     "an exception class called when five division error happens"


# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     if b == 5:
#         raise FiveDivisionError("cannot divide by five")
#     div = a/b
#     print("division is: ", div)

# except (FiveDivisionError, ZeroDivisionError) as var:
#     print(var)

# print("rest of the code")

# -----------------------------------------------
# using constructor

class FiveDivisionError(Exception):
    "an exception class called when five division error happens"

    def __init__(self):
        print("cannot divide by five")
    pass


try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if b == 5:
        raise FiveDivisionError
    div = a/b
    print("division is: ", div)

except (FiveDivisionError, ZeroDivisionError) as var:
    print(var)

print("rest of the code")
