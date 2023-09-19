
# RSA Encryption Program

This project was about learning how the RSA Encryption algorithm works and then implementing it into the following python scripts. In order to complete this project, I had to first generate suplementary programs (primegen and primecheck) that would check if a given number was prime. This was done to check that when the user inputs 2 prime numbers to properly generate their RSA key pairs.

- primecheck.py: The program first imports the required modules, 'random' and 'sys'. Then, it defines the 'miller_rabin' function, which takes two arguments, 'n' and 'rounds'. 'n' is the number that needs to be checked for primality, and 'rounds' is the number of iterations to perform the test. The Miller Rabin test checks the probability that a number is prime using rounds of iterations checking if the number meets the needed prime requirements. Running this program with many rounds makes the probability of the result to be more likely to be correct, which is why the test goes through 10 rounds.

- primegen.py: This program uses the Miller-Rabin primality test to generate a random prime number with a specified number of bits. It takes an integer argument from the command line indicating the number of bits for the prime to be generated. The program creates a random candidate number with the specified number of bits, sets the high-order and low-order bits to 1 to ensure that the number is odd and has the correct number of bits, and performs the Miller-Rabin test on the candidate. If the candidate passes the test, it is returned as the prime number. It should be noted that the generated prime number may not be cryptographically secure and should not be used for sensitive applications without further testing and verification. 

- Keygen.py: This Python program generates a public-private key pair using the RSA algorithm. The program takes two prime numbers 'p' and 'q' as input arguments and returns a tuple containing the public and private keys. It calculates the modulus 'n' and the Euler's totient function 'phi' of 'n' using the provided primes 'p' and 'q'. Then, it selects a public exponent 'e' that is relatively prime to 'phi' and computes the corresponding private exponent 'd' using modular inverse. The program defines helper functions: gcd, which uses the Euclidean algorithm to find the greatest common divisor of two numbers; mod_inverse, which calculates the modular inverse of a number using the extended Euclidean algorithm; and gcdplus, which calculates the extended greatest common divisor of two numbers. In the 'main' function, the program checks if the number of input arguments is correct, extracts the input primes from the command line arguments, and generates an RSA key pair using the provided primes. It then prints the resulting public and private keys. Overall, the program generates an RSA key pair from two provided prime numbers, and the public and private keys can be used for encryption and decryption of messages.

- Encrypt.py: encrypts a plaintext message using the RSA algorithm with a public key. It takes three command-line arguments as inputs: the modulus 'n', the public exponent 'e', and the plaintext message. The program returns the encrypted message as an integer, which is calculated using the pow() function. This function computes the remainder of the plaintext raised to the power of 'e' modulo 'n'. In the 'main' function, the program first checks if the correct number of command-line arguments is provided. If the number of arguments is not equal to four, the program prints a usage message and exits. If there are four arguments, the program parses the arguments as integers and calls the 'rsa_encrypt' function with these values. The encrypted message is then printed to the console.

- Decrypt.py: takes three command-line arguments as inputs: the modulus 'n', the private exponent 'd', and the encrypted message 'ciphertext'. The program returns the decrypted message as an integer, which is calculated using the pow() function. This function computes the remainder of ciphertext raised to the power of 'd' modulo 'n'.In the 'main' function, the program first checks if the correct number of command-line arguments is provided. If there are not exactly four arguments, the program prints a usage message and exits. If there are four arguments, the program parses the arguments as integers and calls the 'rsa_decrypt' function with these values. The decrypted message is then printed to the console.


