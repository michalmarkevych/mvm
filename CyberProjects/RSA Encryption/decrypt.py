import sys

def rsa_decrypt(n, d, ciphertext):
    
    #Decrypt an RSA encrypted message (ciphertext) using private key (n, d).

    # n: The modulus of the RSA key pair
    # d: The private exponent of the RSA key pair
    # ciphertext: The encrypted message (integer)
    # returns  decrypted message (integer)
    
    return pow(ciphertext, d, n)

def main():
    if len(sys.argv) != 4:
        print("Usage: python decrypt.py [n] [d] [ciphertext]")
        sys.exit(1)

    n = int(sys.argv[1])
    d = int(sys.argv[2])
    ciphertext = int(sys.argv[3])

    plaintext = rsa_decrypt(n, d, ciphertext)
    print(plaintext)

if __name__ == "__main__":
    main()
