import hashlib
import rsa
def encode(text, priv_key):
    hash_text = hashlib.sha256(text.encode()).hexdigest()
    cipher_hash = rsa.encrypt(hash_text.encode(), priv_key).hex()
    return cipher_hash
with open('text.txt', 'r', encoding='UTF-8') as file:
    text = file.read()
priv_key, pub_key = rsa.newkeys(1024)
print(f"Текст: {text}\nКлюч: {pub_key}\nПодпись: {encode(text, priv_key)}")
