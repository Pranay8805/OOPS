#1.Write a Python function to multiply all the numbers in a list.
#Sample List : [8, 2, 3, -1, 7]
#Expected Output : -336
def multiply_list(l):
    total = 1
    for x in l:
        total *= x
    return total
print(multiply_list([8,2,3,-1,7]))

