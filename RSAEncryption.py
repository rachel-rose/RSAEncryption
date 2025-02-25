'''
 A function called RSA encrypt which takes as input three integers m, e and N (in this
order), and outputs the ciphertext c which is the encryption of the plaintext m with
the RSA cipher used with public keys e and N.



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

#import random
import math
prime1= math.random() * 100
prime2= math.random() * 100
def RSA_encrypt(m, e, N):
    while is_prime(prime1) == False:
        prime1= math.random() * 100
    
    c= ""
    pass

def convert_to_bits(message):
    totalVal= 0
    for letter in message:
        letVal= #convert letter to binary
        totalVal+=letVal
    pass

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