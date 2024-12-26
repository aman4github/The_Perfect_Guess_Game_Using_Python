import random

n, num, flag = 0, random.randint(1, 10), 0

while n != -1:
    n = int(input("Enter your guess between 1 - 10 (Press -1 to exit): "))
    flag += 1
    if n == -1:
        break
    if n < num:
        print("Higher Number Please...")
    elif n > num:
        print("Lower Number Please...")
    else:
        print(f"Your guess = {n}\nComputer's guess = {num}\n\tYou take {flag} times to perfectly guess")
        break