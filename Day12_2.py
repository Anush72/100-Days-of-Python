# Prime Number Checker


def is_prime(num):
    if num <=1:
        return False
    else:
        for i in range(2,num):
            if num % i == 0:
                print("Not a prime number")
                return False
        return True

a = is_prime(2)
print(a)