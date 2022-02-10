"""
Assignment: Input Validation while Loops Assignment
Program: input_while.py
Author: Colby Boell
Last date modified: 02/10/2022

The purpose of this program is to that prompts the user for numeric input between 1 and 100. Prompt the user until
the input is in the correct range. Once the input is correct, store the input in a list.
"""
# declaring list variable and sentinel value
user_numbers = []
exit_num = 999

# prompts for user input, try and except for if we do not get a number
try:
    number = int(input('Enter a number 1 - 100(999 to exit): '))
except ValueError:
    # prints not valid and sets number to 0 so that it will not add to list
    print('Not Valid')
    number = 0
# while user input does not equal the exit number the while loop runs
while number != exit_num:
    # while the user input isn't a valid number within range, we prompt the user to enter a number
    while not 1 <= number <= 100:
        # try and except if we do not get a number
        try:
            number = int(input('Not in range. Enter a number 1- 100: '))
        except ValueError:
            # prints invalid so and sets number to zero so won't add to list
            print('Not Valid')
            number = 0
    # adds valid number to the list of numbers
    user_numbers.append(number)
    # try and except if we do not get a number
    try:
        number = int(input('Enter a number 1 - 100(999 to exit): '))
    except ValueError:
        # prints invalid so and sets number to zero so won't add to list
        print('Not Valid')
        number = 0

# prints sentence
print('Numbers in list:')
# for each number in the list the for loop prints them out
for num in user_numbers:
    print(num)

"""
Tests:
1.)
Enter a number 1 - 100(999 to exit): 89
Enter a number 1 - 100(999 to exit): 5
Enter a number 1 - 100(999 to exit): f
Not Valid
Not in range. Enter a number 1- 100: f
Not Valid
Not in range. Enter a number 1- 100: 899
Not in range. Enter a number 1- 100: 8
Enter a number 1 - 100(999 to exit): 999
Numbers in list:
89
5
8

2.)
Enter a number 1 - 100(999 to exit): 56
Enter a number 1 - 100(999 to exit): 78
Enter a number 1 - 100(999 to exit): 999
Numbers in list:
56
78

3.)
Enter a number 1 - 100(999 to exit): hi
Not Valid
Not in range. Enter a number 1- 100: 78
Enter a number 1 - 100(999 to exit): r
Not Valid
Not in range. Enter a number 1- 100: 23
Enter a number 1 - 100(999 to exit): 15
Enter a number 1 - 100(999 to exit): 999
Numbers in list:
78
23
15
"""
