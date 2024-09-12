def main():
    result = solv_square()
    if result is not None:
        print(f"Quadratic equation: {result}")


def value():
    # user_input = input("Please enter value of 'a':")
    try:
        global a
        a = int(input("Please enter value of 'a':"))
        global b
        b = int(input("Please enter value of 'b':"))
        global c
        c = int(input("Please enter value of 'c':"))
    except ValueError:
        print("That's not a valid number!")
    global x
    x = b**2-4*a*c
    return (x)


def solv_square():
    result = value()
    if result > 0:
        rivn = a*x**2+b*x+c
    return (rivn)


main()

#test 2nd commit
