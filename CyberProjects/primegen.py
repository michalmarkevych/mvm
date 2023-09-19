import sys
import random

def is_prime_mr(n, k):
    # Base cases
    # 2 and 3 are prime, numbers less than 2 and even numbers are not prime
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Decompose (n - 1) into 2^r * s
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    # Perform k rounds of Miller-Rabin primality test
    #
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits):
    # Keep generating random bit candidates until a prime is found
    while True:
        # Generate a random odd number with the specified number of bits
        candidate = random.getrandbits(bits) | (1 << (bits - 1)) | 1
        # Check if the candidate is prime using the Miller-Rabin primality test
        if is_prime_mr(candidate, 5):
            return candidate

def main():
    if len(sys.argv) != 2:
        print("Usage: python primegen.py [bits]")
        sys.exit(1)

    bits = int(sys.argv[1])
    prime = generate_prime(bits)
    print(prime)

if __name__ == "__main__":
    main()
