# import my_functions

# # Foo function
# def foo():
#     print("Foo")

# # Matplotlib prac
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4]
# y = [1, 3, 8, 4]

# plt.plot(x, y)

# plt.ylabel('Elemental Value')
# plt.xlabel('Element')

# plt.show()

# # OpenPyXL prac
# from openpyxl import Workbook

# import random

# # Create an excel workbook
# work_book = Workbook()

# # Grab the active worksheet
# work_sheet = work_book.active

# # Data can be assigned directly to cells
# work_sheet['A1'] = "This is a test"

# # Rows can also be appended

# for i in range(200):
#     work_sheet.append(["Random number:", random.randrange(1000)])

# work_book.save("Sample.xlsx")