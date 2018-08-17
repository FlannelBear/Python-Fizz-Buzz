def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "Fizz Buzz"
    elif n % 5 == 0:
        return "Buzz"
    elif n % 3 == 0:
        return "Fizz"
    else:
        return n

for x in range(1, 51):
    fizz_buzz(x)

