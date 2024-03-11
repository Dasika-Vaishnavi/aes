# import aes

# # Your custom key as an integer
# custom_key = 0x000102030405060708090a0b0c0d0e0f
# plaintext = "00112233445566778899aabbccddeeff"

# # Convert the custom key and plaintext to bytes
# key_bytes = custom_key.to_bytes(16, byteorder='big')
# plaintext_bytes = bytes.fromhex(plaintext)

# # Create an instance of the aes class with your custom key
# cipher = aes.aes(custom_key, 128)

# # Convert plaintext_bytes to a list of integers
# plaintext_list = list(plaintext_bytes)

# # Now you can use the `cipher` object for encryption
# encrypted = cipher.encrypt(plaintext_list)
# print(encrypted)

# encrypted_bytes = bytes(encrypted)

# # Convert the bytes to a hexadecimal string
# encrypted_hex = encrypted_bytes.hex()

# print(encrypted_hex)

import aes

def encrypt_aes(custom_key, plaintext):
    # Convert the custom key and plaintext to bytes
    key_bytes = custom_key.to_bytes(16, byteorder='big')
    plaintext_bytes = bytes.fromhex(plaintext)

    # Create an instance of the aes class with your custom key
    cipher = aes.aes(custom_key, 128)

    # Convert plaintext_bytes to a list of integers
    plaintext_list = list(plaintext_bytes)

    # Now you can use the `cipher` object for encryption
    encrypted = cipher.encrypt(plaintext_list)

    # Convert the list of integers to bytes
    encrypted_bytes = bytes(encrypted)

    # Convert the bytes to a hexadecimal string
    encrypted_hex = encrypted_bytes.hex()

    return encrypted_hex

# Usage
custom_key = 0x000102030405060708090a0b0c0d0e0f
plaintext = "00112233445566778899aabbccddeeff"
# expected output => "round[10].output 69c4e0d86a7b0430d8cdb78070b4c55a

print(encrypt_aes(custom_key, plaintext))