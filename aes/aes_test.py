import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


import aes

def encrypt_aes(custom_key, plaintext, keysize):
    # Calculate the number of bytes from the keysize (e.g., 128 bits -> 16 bytes)
    key_bytes_length = keysize // 8

    # Convert the custom key and plaintext to bytes with the correct length
    key_bytes = custom_key.to_bytes(key_bytes_length, byteorder='big')
    plaintext_bytes = bytes.fromhex(plaintext)

    # Create an instance of the aes class with your custom key
    cipher = aes.aes(int.from_bytes(key_bytes, byteorder='big'), keysize)

    # Convert plaintext_bytes to a list of integers
    plaintext_list = list(plaintext_bytes)

    # Now you can use the `cipher` object for encryption
    encrypted = cipher.encrypt(plaintext_list)

    # Convert the list of integers to bytes
    encrypted_bytes = bytes(encrypted)

    # Convert the bytes to a hexadecimal string
    encrypted_hex = encrypted_bytes.hex()

    return encrypted_hex

# Checking with NIST codes

# For AES 128
custom_key = 0x000102030405060708090a0b0c0d0e0f
plaintext = "00112233445566778899aabbccddeeff"
keysize = 128
print(encrypt_aes(custom_key, plaintext, keysize))

# For AES 192
key = 0x000102030405060708090a0b0c0d0e0f1011121314151617
plaintext = "00112233445566778899aabbccddeeff"
keysize = 192
print(encrypt_aes(key, plaintext, keysize))

# For AES 256
key = 0x000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f
plaintext = "00112233445566778899aabbccddeeff"
keysize = 256
print(encrypt_aes(key, plaintext, keysize))
