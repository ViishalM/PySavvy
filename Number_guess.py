import random
import math

lower = int(input("Enter the Lower bound: "))
upper = int(input("Enter the Upper bound: "))
x = random.randint(lower, upper)
max = round(math.log(upper-lower+1, 2))
print(f"You have {max} tries to guess the number")

count = 0

while count < max:
    count += 1
    guess = int(input("Guess a number: "))
    if x == guess:
        print("Congratulations, You guessed it right in ", count, " try")
        break
    elif x > guess:
        print("You guessed too small")
    elif x < guess:
        print("You guessed too high")

if count >= max:
    print(f"The number is {x}")
    print(f"You guessed it in {count} tries")
