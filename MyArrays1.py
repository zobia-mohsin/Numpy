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

arr09 = np.linspace(0.0, 1.0, num=5)

arr10 = np.arange(1, 21).reshape(4, 5)
# to reshape something make wsure it is the right sice

num01 = np.arange(1, 6)

num02 = num01 * 2
#num02 = num01 [2, 2, 2, 2, 2]
# unequal arrays broadcasting value

num03 = num01 ** 3

num01 += 10
# this is changing the original arrays,
# but broadcasting does not change the orginal arrays

num04 = num01 * num02
# this will only work if those two arrays have same size and shape

num05 = num01 > 13

num06 = num03 > num01  # returns true and false
# building blocks of pandas

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

print(grades.sum())
print(grades.mean())
print(grades.std())
print(grades.var())

grades_by_exam = grades.mean(axis=0)

grades_by_student = grades.mean(axis=1)

num07 = np.array([1, 4, 9, 16, 25, 36])
num08 = np.sqrt(num07)

num09 = np.array([10, 20, 30, 40, 50, 60])
num10 = np.add(num07, num09)

num11 = np.multiply(num09, 5)

num12 = num09.reshape(2, 3)  # three rows of two columns
num13 = np.array([2, 4, 6])

# num12 and num13 have different shapes, would that work?
# works because number of columns match (to multiply)
num14 = np.multiply(num12, num13)


print()


# print()  # start using debugger, shape tells you 2 rows 3 columns, size tells how many total elements
