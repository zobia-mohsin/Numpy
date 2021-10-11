import numpy as np


# Here we have an array of 4 students of 4 students grades on 3 exams
# row = each student(student0,student1, studetn2, studetn3)
# COLS = eact test (test0, test1,test2)

grades = np.array([[87, 96, 70], [100, 87, 90],
                   [94, 77, 90], [100, 81, 82]])

# Indexing and Slicing, look at particular rows and slice accordingly

student1 = grades[1]

student0_test1 = grades[0, 1]

# sequential rows use columns, upper bound not included
# colons mean consecutive rows : but commas to separate them
students0_1 = grades[0:2]

# outer brackets row and column, inner brackets 1 and 3 rows
students1and3 = grades[[1, 3]]
# want particular column as , and specify column you want
students1and3_test2 = grades[[1, 3], 2]
# first element is rows so colons mean all rows, column 0
all_students_test0 = grades[:, 0]

# upper bound 3 is not included gives test 1 and 2
all_students_test1_2 = grades[:, 1:3]

all_students_test0and2 = grades[:, [0, 2]]


# EXERCISE
grades = np.random.randint(60, 101, 12).reshape(3, 4)  # 101 to INCLUDE 100

grades.mean()

# by col
grades.mean(axis=0)

# by row
grades.mean(axis=1)

numbers = np.arange(1, 6)

numbers_view = numbers.view()

numbers[1] *= 10

# change view to get back array, CHANGE IN ONE EFFECTS OTHER SHALLOW COPY .view()
numbers_view[1] /= 10

# slice effects the original array too
numbers_slice_view = numbers[0:3]

# when you are working with indexes, usually start with index 0
numbers[1] *= 20

# deep copy does not effect the orginal copy, .copy() VIEW AND SLICE DOES THE SAME THING
numbers_copy = numbers.copy()

numbers[1] *= 10

grades = np.array([[87, 96, 70], [100, 87, 90]])

# creates a shallow copy
grades_reshaped = grades.reshape(1, 6)

# modifies the original array, not necessarily a deep copy
#grades.resize(1, 6)

# Method flatten deep copies the original array's data:
# always one dimensional array
flattened = grades.flatten()
# alternatively, Methods ravel produces a view (shallow copy) of the original array
# which shares the grades array's data:

raveled = grades.ravel()

raveled[0] = 100

raveled[5] = 99

print()  # run and debug values seen in debug
