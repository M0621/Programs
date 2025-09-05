import random

#RSA algorithm

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num // 2 + 1):
        if num % i == 0:
            return False
    return True
    
def generate_prime(min,max):
    prime = random.randint(min,max)
    while not is_prime(prime):
        prime = random.randint(min,max)
    return prime

def eulers_toshian(p,q):
    return (p-1) * (q-1)

def public_key(phi):
    while True:
        e = random.randint(2,phi - 1)
        temp = e
        temp1 = phi
        while temp != 0:
            rem = temp1 % temp
            temp1 = temp
            temp = rem
        gcd = temp1
        if gcd == 1:
            return e

def private_key(e,phi):
    for d in range(3,phi):
        if (e*d) % phi == 1:
            return d
    raise ValueError("MOD inverse does not exist")

p , q = generate_prime(100,1000),generate_prime(100,1000)

while p == q:
    q = generate_prime(100,1000)

n = p * q

phi = eulers_toshian(p,q)

e = public_key(phi)

d = private_key(e,phi)

message = "Hello World"

message_encoded = [ord(ch) for ch in message]

ciphertext = [pow(ch,e,n) for ch in message_encoded]

message_encoded = [pow(ch,d,n) for ch in ciphertext]

plaintext = "".join(chr(ch) for ch in message_encoded)

message_encoded = [ord(ch) for ch in message]

signature = [pow(ch,d,n) for ch in message_encoded] 

verify_signature = [pow(ch,e,n) for ch in signature]

print("Public Key:",e)
print("Private Key:",d)
print("n:",n)
print("Phi of n:",phi)
print("p:",p)
print("q:",q)
print("Message:",message)
print("Encrypted Message:",ciphertext)
print("Decrypted Message:",plaintext)
print("Signature:",signature)


if [ord(ch) for ch in message] == verify_signature:
    print("Signature Verfied")
else:
    print("Incorrect Signature")




