# 1. printing exception name
# two methods, using:
# i. exception class object
# ii. sys module

# a = int(input("enter first no: "))
# b = int(input("enter sedond no: "))


# try:
#     div = a/b
#     print("ans is: ", div)
# except ZeroDivisionError as obj:  # way of writing pt1
#     print(obj)
# except NameError as var:  # way of writing pt2 to write the class of the error
#     print(var.__class__)
# except Exception as obj:  # way of writing pt1
#     print(obj)


# print("rest of the code")

# --------------------------------------------------------

# using sys module

import sys
a = int(input("enter first no: "))
b = int(input("enter sedond no: "))


try:
    div = a/b
    print("ans is: ", div)
except:
    print(sys.exc_info()[0])  # <class of exception>
    print(sys.exc_info()[1])  # <discription of exception>


print("rest of the code")

# ---------------------------------------------------------
