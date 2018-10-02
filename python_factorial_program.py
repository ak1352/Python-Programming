def factorial(number):
    factorial = 1
    for i in range(1,number+1):
        if number == 0:
            factorial = 1
        else:
            factorial= factorial*i
    return factorial
factorial(5)