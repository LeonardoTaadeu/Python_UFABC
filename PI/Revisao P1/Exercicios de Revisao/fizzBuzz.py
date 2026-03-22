def fizzbuzz(a):
    if a % 3 == 0 and a % 5 == 0:
        return ("fizzbuzz")
    elif a % 5 == 0:
        return ("buzz")
    elif a % 3 == 0: 
        return ("fizz")
    else:
        return a