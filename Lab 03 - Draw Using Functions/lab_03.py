# # This function will print the result
# def sum_print(a, b):
#     result = a + b
#     print(result)


# # This function will return the result
# def sum_return(a, b):
#     result = a + b
#     return result


# # This code prints the sum of 4+4, because the function has a print
# sum_print(4, 4)

# # This code prints nothing, because the function returns, and doesn't print
# sum_return(4, 4)

# # This code will not set x1 to the sum.
# # The sum_print function does not have a return statement, so it returns
# # nothing!
# # x1 actually gets a value of 'None' because nothing was returned
# x1 = sum_print(4, 4)
# print("x1 =", x1)

# # This will set x2 to the sum and print it properly.
# x2 = sum_return(4, 4)
# print("x2 =", x2)

# Create the x variable and set to 44
x = 44


# Define a simple function that prints x
# def f():
#     x += 1
#     print(x)


# # Call the function
# f()

# Define a simple function that prints x
# def f(x):
#     x += 1
#     print(x)


# # Set y
# y = 10
# # Call the function
# f(y)
# # Print y to see if it changed
# print(y)

# Define a simple function that prints x
# def f(x):
#     x += 1
#     print(x)


# # Set x
# x = 10
# # Call the function
# f(x)
# # Print x to see if it changed
# print(x)

# Example 5
# def a(x):
#     print("A start, x =", x)
#     b(x + 1)
#     print("A end, x =", x)


# def b(x):
#     print("B start, x =", x)
#     c(x + 1)
#     print("B end, x =", x)


# def c(x):
#     print("C start and end, x =", x)


# a(5)

# Example 8
# def a(x):
#     x = x + 1
#     return x


# x = 3
# x = a(x)

# print(x)

# Example 14
def a(my_list):
    print("function a, list =  ", my_list)
    my_list = [10, 20, 30]
    print("function a, list =  ", my_list)


my_list = [5, 2, 4]

print("global scope, list =", my_list)
a(my_list)
print("global scope, list =", my_list)