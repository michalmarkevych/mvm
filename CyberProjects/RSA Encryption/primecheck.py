#importing random and sys
import random
import sys

#using miller_rabin test
#will return true if n has a high probability of being prime
#will return false if the number has a high probability of being composite
def miller_rabin(n, rounds):
    #need to make a defined case for small numbers
    if n < 2:
        return False
    if n==2:
        return True
    if n==3:
        return True

#general case
#expon= the exponenet
#remain= the remainder  
    expon, remain = 0, n - 1
    while remain % 2 == 0:
        expon += 1
        remain //= 2
#goes for a certain amount of rounds
    for _ in range(rounds):
        base = random.randrange(2, n - 1)
        result = pow(base, remain, n)
        if result == 1 or result == n - 1:
            continue
        for _ in range(expon - 1):
            result = pow(result, 2, n)
            if result == n - 1:
                break
        else:
            return False
    return True

#making the code into a script
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python primecheck.py [number]")
        sys.exit(1)

    number = int(sys.argv[1])
    output = miller_rabin(number, 10)
    print(output)
