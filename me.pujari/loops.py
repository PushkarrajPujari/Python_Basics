# The for statement in Python differs a bit from what you may be used to in C or Pascal.
# Rather than always iterating over an arithmetic progression of numbers (like in Pascal),
# or giving the user the ability to define both the iteration step and halting condition (as C),
# Python’s for statement iterates over the items of any sequence (a list or a string),
# in the order that they appear in the sequence.
# This description is taken from python docs

# If you do need to iterate over a sequence of numbers,
# the built-in function range() comes in handy. It generates arithmetic progressions:

for i in range(5):
    print(i)

print("----------------------------------------------------")

for i in range(5, 10):
    print(i)

print("----------------------------------------------------")

for i in range(0, 10, 2):
    print(i)
