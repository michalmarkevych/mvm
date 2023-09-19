import sys

def rsa_keygen(p, q):
    
    # Generate an RSA key pair given two prime numbers p and q.
    # p: A prime number
    # q: A prime number
    # returns a tuple containing the public key and private key as (n, e) and (n, d) pairs
    
    n = p * q
    phi = (p - 1) * (q - 1)

    # Find a public exponent e such that gcd(e, phi) = 1
    e = 3
    while gcd(e, phi) != 1:
        e += 2

    # Calculate the private exponent d using modular inverse
    d = mod_inverse(e, phi)

    return (n, e), (n, d)

def gcd(a, b):
    
    #Calculates the greatest common divisor of two numbers using the Euclidean algorithm.
    # where a is an integer, b is an integer, and the function returns the greatest common divider
    
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    
    #Calculate the modular inverse of a modulo m where a is an integer and will return the modular inverse of mod m
    
    g, x, y = gcdplus(a, m)
    if g != 1:
        raise Exception('No modular inverse exists')
    return x % m

def gcdplus(a, b):
    
    #need to calculate the extended greatest common divisor of two numbers.
    # in this function a is integer, b is an integer, and function returns a tuple of the greatest common divisor along with x and y
    
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = gcdplus(b % a, a)
        return g, y - (b // a) * x, x

def main():
    if len(sys.argv) != 3:
        print("Usage: python keygen.py [prime1] [prime2]")
        sys.exit(1)

    prime1 = int(sys.argv[1])
    prime2 = int(sys.argv[2])

    # Generate RSA key pair using the provided prime numbers
    public_key, private_key = rsa_keygen(prime1, prime2)

    print("Public Key:", public_key)
    print("Private Key:", private_key)

if __name__ == "__main__":
    main()
