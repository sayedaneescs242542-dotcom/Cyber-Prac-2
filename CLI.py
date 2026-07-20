from math import gcd

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d

# Input primes
p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))

n = p * q
phi = (p - 1) * (q - 1)

e = 17

while gcd(e, phi) != 1:
    e += 2

d = mod_inverse(e, phi)

print("\nPublic Key:", (e, n))
print("Private Key:", (d, n))

message = int(input("\nEnter message: "))

cipher = pow(message, e, n)
print("Encrypted Message:", cipher)

decrypted = pow(cipher, d, n)
print("Decrypted Message:", decrypted)