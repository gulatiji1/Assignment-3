def factorial(number):
    fact=1
    if number==1:
        return 1
    else:
        while number>1:
            fact=fact*number
            number=number-1

    print(f"Factorial of {num} is {fact}")

num=int(input("Enter a number:"))
factorial(num)
