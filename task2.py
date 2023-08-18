def prime(num1):
    counter = 0
    i = 3
    if num1 == 2:
        return ("PRIME")
    elif num1 < 2:
        return ("NOT PRIME")

    else:
        while i <= (num1/2):
            if num1 % i == 0:
                counter = 1
                break
            else:
                i += 1
                counter = 0
        if counter == 1:
            return ("NOT PRIME")
        else:
            return ("PRIME")


num2 = int(input("the number"))
print(prime(num2))
print("thx :)")
