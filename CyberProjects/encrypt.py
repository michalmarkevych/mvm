import sys

def rsa_encrypt(n, e, plaintext):
    
    # Encrypt a message (plaintext) using RSA public key (n, e).
    # n: The modulus of the RSA key pair
    # e: The public exponent of the RSA key pair
    # plaintext: The message to be encrypted (integer)
    # returns encrypted message (integer)
    
    return pow(plaintext, e, n)

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python encrypt.py [n] [e] [plaintext]")
        sys.exit(1)
    # Parse the command-line arguments as integers
    n = int(sys.argv[1])
    e = int(sys.argv[2])
    plaintext = int(sys.argv[3])

    # Encrypt the plaintext using the RSA public key (n, e)
    ciphertext = rsa_encrypt(n, e, plaintext)
    print(ciphertext)

if __name__ == "__main__":
    main()
