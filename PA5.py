import random 
from math import pow as pper

a = random.randint(2, 10)

def gcd(a, b):

    if a >= b:
        if a%b == 0:
            return b
        return gcd(b,a%b)

    return gcd(b,a)

def gen_key(q):

    key = random.randint(pper(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pper(10, 20), q)
    return key


def power(a, b, c):
    if b == 0:
        return 1
    x = power(a,b//2,c)
    y = 1
    if b&1:
        y = a
    y = (x * x * y)%c
    return y
# Asymmetric encryption

def encrypt(msg, q, h, g):
    encrypted_msg = []
    k = gen_key(q)# Private key for sender
    s = power(h, k, q)
    p = power(g, k, q)

    for i in range(0, len(msg)):
        encrypted_msg.append(msg[i])
 
    print("g^k used : ", p)

    print("g^ak used : ", s)
    for i in range(len(encrypted_msg)):
        encrypted_msg[i] = s * ord(encrypted_msg[i])
    return encrypted_msg, p

def decrypt(encrypted_msg, p, key, q):
    decrypted_msg = []
    h = power(p, key, q)
    for i in range(0, len(encrypted_msg)):

        decrypted_msg.append(chr(int(encrypted_msg[i]/h)))

    return decrypted_msg
 
# Driver code

def main():
    msg = 'Divyansh'
    print("Original Message :", msg)

    q = random.randint(pper(10, 20), pper(10, 50))
    g = random.randint(2, q)

    key = gen_key(q)# Private key for receiver
    h = power(g, key, q)
    print("value of g : ", g)
    print("value of g^a : ", h)

    encrypted_msg, p = encrypt(msg, q, h, g)

    decrypted_msg = decrypt(encrypted_msg, p, key, q)

    dmsg = ''.join(decrypted_msg)

    print("Decrypted Message :", dmsg);

if __name__ == '__main__':

    main()