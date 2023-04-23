
import hashlib, json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES


## -------- encrypt / decrypt ----------- ##
def encrypt(wordList):
    # generate a random salt
    salt = b"UkXp2s5v8y/B?D(G+KbPeShVmYq3t6w9"
    password = "key"
    # use the Scrypt KDF to get a private key from the password
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    # create cipher config
    cipher_config = AES.new(private_key, AES.MODE_GCM)
    cipher_text, tag = cipher_config.encrypt_and_digest(bytes(wordList, "utf-8"))
    # return a dictionary with the encrypted text
    dict = {
        "cipher_text": b64encode(cipher_text).decode("utf-8"),
        "nonce": b64encode(cipher_config.nonce).decode("utf-8"),
        "tag": b64encode(tag).decode("utf-8")
    }
    return str(dict).replace('\'' , "\"")

def decrypt(enc_dict):

    # decode the dictionary entries from base64
    enc_dict = json.loads(enc_dict)
    salt = b"UkXp2s5v8y/B?D(G+KbPeShVmYq3t6w9"
    cipher_text = b64decode(enc_dict["cipher_text"])
    nonce = b64decode(enc_dict["nonce"])
    tag = b64decode(enc_dict["tag"])
    password = "key"

    # generate the private key from the password and salt
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    # create the cipher config
    cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

    # decrypt the cipher text
    decrypted = cipher.decrypt_and_verify(cipher_text, tag)

    return decrypted.decode("utf-8")