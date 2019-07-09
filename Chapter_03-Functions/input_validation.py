# Input Validation

"""Add try and except statements to the previous project to detect whether
the user types in a noninteger string. Normally, the int() function will
raise a ValueError error if it is passed a noninteger string, as in
int('puppy'). In the except clause, print a message to the user saying
they must enter an integer."""

# The Collatz Sequence

""" Write a function named collatz() that has one parameter named number.
If number is even, then collatz() should print number // 2 and return this
value. If number is odd, then collatz() should print and return 3 * number + 1."""

""" Then write a program that lets the user type in an integer and that keeps
calling collatz() on that number until the function returns the value 1.
(Amazingly enough, this sequence actually works for any integer—sooner or
later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t
sure why. Your program is exploring what’s called the Collatz sequence,
sometimes called “the simplest impossible math problem.”)"""

"""Remember to convert the return value from input() to an integer with the
int() function; otherwise, it will be a string value."""


def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number %2 != 0:
        return 3 * number + 1

print('Enter number:')
try:
    num = int(input())
except:
    ValueError
    
while num > 1:
    num = collatz(num)
    print(num)
