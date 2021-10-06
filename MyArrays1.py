import numpy as np
import random
# This is two rows and one column, 2 dimensional array.
arr01 = np.array([[1, 2, 3], [4, 5, 6]])
# EACH SET REPRESENTS A ROW, WITHIN EACH SQUARE BRAKETS IS A COLUMN

# the bottom one is one dimensional
arr02 = np.array([0.0, 0.1, 0.2, 0.3, 0.4])

'''
for row in arr01:
    print(row)
    input()
    for col in row:
        print(col, end=' ')  # end = space to make spaces in output,
    print()                                       # This waiting to hit enter in input

for i in arr01.flat:  # flat options does not care about dimensions, flat goes through all
    print(i)
'''
arr03 = np.zeros(5)  # one dimensional of 5 zeros

arr04 = np.ones((2, 4), dtype=int)  # 2 rows of 4 columns in intgers

arr05 = np.full((3, 5), 13)  # three rows of 5 column each of the number 13
# default of arrow is FLOAT

print()  # start using debugger, shape tells you 2 rows 3 columns, size tells how many total elements


# exercise
# i in range 5 means loop 5 times, random int from 1 thorugh 10
a = np.array([[random.randint(1, 10) for i in range(5)],
             [random.randint(1, 10) for i in range(5)]])

b = np.array(np.random.randint(1, 10, size=(2, 5)))

arr06 = np.arange(5)

arr07 = np.arange(5, 10)  # lower and upper bounds of arrange

arr08 = np.arange(10, 1, -2)


print()  # start using debugger, shape tells you 2 rows 3 columns, size tells how many total elements
