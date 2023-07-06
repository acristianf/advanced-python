# regular assignment operation
x = 5
print(x)

# assignment operator as part of an expression(walrus operator)
(z := 8)
print(z)
if y := 5:
    print(y)

# the walrus operator works well to create concise code
# while (thestr := input("Value? ") != "exit"):
#     print(thestr)

# Helps reduce redundant function calls
values = [10, 1, 23, 123, 0, 3, 4, 9]
val_data = {
    "length": (l := len(values)),
    "total": (s := sum(values)),
    "average": s / l
}

__import__('pprint').pprint(val_data)
