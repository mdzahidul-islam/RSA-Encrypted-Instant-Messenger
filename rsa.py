import random
import sys
import math

from random import randrange

def rabinMiller(n, k=10):
    if n == 2:
            return True
    if not n & 1:
            return False

    def check(a, s, d, n):
            x = pow(a, d, n)
            if x == 1:
                    return True
            for i in range(1, s - 1):
                    if x == n - 1:
                            return True
                    x = pow(x, 2, n)
            return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
            d >>= 1
            s += 1

    for i in range(1, k):
            a = randrange(2, n - 1)
            if not check(a, s, d, n):
                    return False
    return True

def isPrime(n):
     #lowPrimes is all primes (sans 2, which is covered by the bitwise and operator)
     #under 1000. taking n modulo each lowPrime allows us to remove a huge chunk
     #of composite numbers from our potential pool without resorting to Rabin-Miller
     lowPrimes =   [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
                   ,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179
                   ,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269
                   ,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367
                   ,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461
                   ,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571
                   ,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661
                   ,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773
                   ,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883
                   ,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
     if (n >= 3):
         if (n&1 != 0):
             for p in lowPrimes:
                 if (n == p):
                    return True
                 if (n % p == 0):
                     return False
             return rabinMiller(n)
     return False

def generateLargePrime(k):
     #k is the desired bit length
     r = 100*(math.log(k,2)+1) #number of attempts max
     r_ = r
     while r>0:
        #randrange is mersenne twister and is completely deterministic
        #unusable for serious crypto purposes
         n = random.randrange(2**(k-1),2**(k))
         r -= 1
         if isPrime(n) == True:
             return n

     str_failure = "Failure after" + str(r_) + "tries."
     return str_failure


def gcd(a, b):
    '''
    Euclid's algorithm for determining the greatest common divisor
    Use iteration to make it faster for larger integers
    '''
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(a, b):
    """Returns a tuple (r, i, j) such that r = gcd(a, b) = ia + jb
    """
    # r = gcd(a,b) i = multiplicitive inverse of a mod b
    #      or      j = multiplicitive inverse of b mod a
    # Neg return values for i or j are made positive mod b or a respectively
    # Iterateive Version is faster and uses much less stack space
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a  # Remember original a/b to remove
    ob = b  # negative values from return results
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob  # If neg wrap modulo orignal b
    if ly < 0:
        ly += oa  # If neg wrap modulo orignal a
    # return a , lx, ly  # Return only positive values
    return lx

def multiply(x, y):
    _CUTOFF = 1536
    if x.bit_length() <= _CUTOFF or y.bit_length() <= _CUTOFF:  # Base case
        return x * y
    else:
        n = max(x.bit_length(), y.bit_length())
        half = (n + 32) // 64 * 32
        mask = (1 << half) - 1
        xlow = x & mask
        ylow = y & mask
        xhigh = x >> half
        yhigh = y >> half

        a = multiply(xhigh, yhigh)
        b = multiply(xlow + xhigh, ylow + yhigh)
        c = multiply(xlow, ylow)
        d = b - a - c
        return (((a << half) + d) << half) + c


def generate_keypair(keySize=10):
    p = generateLargePrime(keySize)
    # print(p)
    q = generateLargePrime(keySize)
    # print(q)
    # p = 997
    # q = 271

    if p == q:
        raise ValueError('p and q cannot be equal')

    #n = pq
    n = multiply(p, q)

    #Phi is the totient of n
    phi = multiply((p-1),(q-1))

    #Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)

    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    #Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    #Unpack the key into it's components
    key, n = pk
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    # cipher = [(ord(char) ** key) % n for char in plaintext]
    #Return the array of bytes   [pow(ord(char),key,n) for char in plaintext]
    cipher = [format(pow(ord(char),key,n),'08d') for char in plaintext]
    return ''.join(map(lambda x: str(x), cipher))


def decrypt(pk, ciphertext):
    #Unpack the key into its components
    key, n = pk
    ciphertext = [int(ciphertext[i:i + 8]) for i in range(0, len(ciphertext), 8)]
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)

public1, private1 = generate_keypair()
public2, private2 = generate_keypair()

# if __name__ == '__main__':
#     '''
#     Detect if the script is being run directly by the user
#     '''
#     print("RSA Encrypter/ Decrypter")
#
#     print("Generating your public/private keypairs now . . .")
#     public, private = generate_keypair()
#     print("Your public key is ", public ," and your private key is ", private)
#
#     message = str(sys.argv[1])
#
#     encrypted_msg = encrypt(public, message)
#
#     print("Your encrypted message is: " + encrypted_msg)
#     # print(''.join(map(lambda x: str(x), encrypted_msg)))
#     print("Decrypting message with public key ", public ,"...")
#     print("Your message is:")
#     print(decrypt(private, encrypted_msg))