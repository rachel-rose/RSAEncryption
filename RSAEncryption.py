'''
 A function called RSA encrypt which takes as input three integers m, e and N (in this
order), and outputs the ciphertext c which is the encryption of the plaintext m with
the RSA cipher used with public keys e and N.

c=cyphertext
m= plaintext
e, N= public keys

#multiply two primes togther- they are kept secret
    #encrypted by anyone- public key
    #decrypted  by priv key
#decryption is factoring
#math.random
#check for primes

#Convert the ASCII string into an array of bytes. ones and zeros
#Convert that byte array into a large integer
#multiple

'''

def RSA_encrypt(m: int, e: int, N: int) -> int:
    # Ensure m is within valid range
    if not (0 <= m < N):
        raise ValueError("Plaintext must be in the range 0 <= m < N")
    # RSA encryption using modular exponentiation
    c = pow(m, e, N)   
    return c


m = 42  # plaintext message
e = 65537  # common public exponent
N = 3233  # example modulus (should be the product of two primes in real RSA)
    
ciphertext = RSA_encrypt(m, e, N)
print(f"Ciphertext: {ciphertext}")
'''-----------------------------------------------------------------------------------------------'''


'''
prime1= math.random() * 100
prime2= math.random() * 100
def RSA_encrypt(m: int, e: int, N: int) -> int:
    while is_prime(prime1) == False:
        prime1= math.random() * 100
    while is_prime(prime2) == False:
        prime2= math.random() * 100
    str_as_binary = str_to_binary(m)
    prime1*prime2
    c= ""
    pass

#https://www.geeksforgeeks.org/python-convert-string-to-binary/ 
def str_to_binary(string):
    # Initialize empty list to store binary values
    binary_list = []
     
    # Iterate through each character in the string
    for char in string:
        # Convert character to binary, pad with leading zeroes and append to list
        binary_list.append(bin(ord(char))[2:].zfill(8))
         
    # Join the binary values in the list and return as a single string
    return ''.join(binary_list)


#source: https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
def is_prime(num):
    if num > 1:

        # Iterate from 2 to n // 2
        for i in range(2, (num//2)+1):
        
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            return True
    else:
        return False
  '''
