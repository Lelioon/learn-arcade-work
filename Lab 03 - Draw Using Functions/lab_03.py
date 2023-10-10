# This function will print the result
def sum_print(a, b):
    result = a + b
    print(result)


# This function will return the result
def sum_return(a, b):
    result = a + b
    return result


# This code prints the sum of 4+4, because the function has a print
sum_print(4, 4)

# This code prints nothing, because the function returns, and doesn't print
sum_return(4, 4)

# This code will not set x1 to the sum.
# The sum_print function does not have a return statement, so it returns
# nothing!
# x1 actually gets a value of 'None' because nothing was returned
x1 = sum_print(4, 4)
print("x1 =", x1)

# This will set x2 to the sum and print it properly.
x2 = sum_return(4, 4)
print("x2 =", x2)