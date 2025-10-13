"""
 Write your own python program for computing square roots that implements Newton’s Method.  Use of inbuilt function,
 math library or x**0.5 is not allowed.
 Newton Method is a category of guess-and-check approach. You first guess what the square root might be and then see
 how close your guess is. You can use this information to make another guess and continue guessing until you have found
 the square root (or a close approximation to it). Suppose x is the number we want the root of and guess is the current
 guessed answer. The guess can be improved by using (guess+ x/guess)/2 as the next guess.
 The program should -
 1.Prompt the user for the value to find the square root of (x) and the number of mes to improve the guess.
 2.Star ng with a guess value of x/2, your program should loop the specified number of mes applying Newton’s method
 and report the final value of guess.
"""
number = float(input("Enter number :"))
guess = number / 2
fix = 0
while guess<=number:
    if guess * guess == number:
        print(guess)
        break
    else:
        fix = guess
        guess = (guess + number / guess) / 2
        if fix == guess:
            break