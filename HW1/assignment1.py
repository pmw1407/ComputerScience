import crypto 
import sys 
sys.modules['Crypto'] = crypto
from Crypto.Cipher import DES
import hashlib
import random

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

#문자열을 8바이트 배수 단위로 만드는 함수
def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


class DESCipher:
    def __init__(self, key):
        self.key = key
        self.descipher = DES.new(key, DES.MODE_ECB)
    
    def encrypt(self, text):
        padded_text = pad(text)
        encrypted_text = self.descipher.encrypt(padded_text.encode())
        print("DES Encrypted :", encrypted_text)
        return encrypted_text

    def decrypt(self, encrypted_text):
        decrypted_text = self.descipher.decrypt(encrypted_text)
        print("DES Decrypted : " + decrypted_text.decode())


class HashEncrypt:
    def __init__(self):
        self.m = hashlib.sha256()

    def encrypt(self, text):
        btext = text.encode()
        self.m.update(btext)
        print("Hash type : SHA256")
        print("Hash Encrypted :", self.m.digest())


class RSACipher:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.n = p * q
        self.totient = (p - 1) * (q - 1)
        print("p :", p)
        print("q :", q)

    def get_private_key(self, e):
        k = 1
        while (e * k) % self.totient != 1 or k == e:
            k += 1
        print("private key :", k)
        return k

    def get_public_key(self):
        e = 2
        while e < self.totient and gcd(e, self.totient) != 1:
            e += 1
        print("public key :", e)
        return e

    def encrypt(self, pk, plaintext):
        key, n = pk
        encrypted_text = [(ord(char) ** key) % n for char in plaintext]
        print("RSA Encrypted :", encrypted_text)
        return encrypted_text

    def decrypt(self, pk, encrypted_text):
        key, n = pk
        decrypted_text = [chr((char ** key) % n) for char in encrypted_text]
        return ''.join(decrypted_text)

    

# 원본 문자열
text = input("Original data : ")

# 8바이트 키
key = input("key(8 byte) for DES : ").encode()

des = DESCipher(key)
encrypted_text = des.encrypt(text)
des.decrypt(encrypted_text)

hashencrypt = HashEncrypt()
hashencrypt.encrypt(text)

p = random.choice(prime)
q = random.choice(prime)
rsa = RSACipher(p, q)
e = rsa.get_public_key()
d = rsa.get_private_key(e)
rsa_encrypted_text = rsa.encrypt((e, rsa.n), text)
print("RSA Encrypted :", ''.join(map(lambda  x: str(x), rsa_encrypted_text)))
print("RSA Decrypted :", rsa.decrypt((d, rsa.n), rsa_encrypted_text))