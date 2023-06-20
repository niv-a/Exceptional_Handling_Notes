# using "raise" in various ways
# ----------------------------

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError()
    print("your age is: ", age)
except ValueError:
    print("Enter valid age")

print("rest of the code")

# ------------------------------------

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Invalid age")
    print("your age is: ", age)
except ValueError as var:
    print(var)

print("rest of the code")
