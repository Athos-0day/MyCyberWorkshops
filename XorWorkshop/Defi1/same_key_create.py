# Clé en binaire 
KEY_BITS = [
    0b01001101,  
    0b01111001,  
    0b01001011,  
    0b01100101,  
    0b01111001   
]

# Message 1 
PLAINTEXT1_BITS = [
    0b01001110,  
    0b01100101, 
    0b01110100,  
    0b00110111   
]

# Message 2 
PLAINTEXT2_BITS = [
    0b01010000,  
    0b01101111,  
    0b01101110,  
    0b01111001,  
    0b00110111   
]


def xor_encrypt_bytes(plaintext_bits, key_bits):
    return bytes(
        plaintext_bits[i] ^ key_bits[i % len(key_bits)]
        for i in range(len(plaintext_bits))
    )


cipher1 = xor_encrypt_bytes(PLAINTEXT1_BITS, KEY_BITS)
cipher2 = xor_encrypt_bytes(PLAINTEXT2_BITS, KEY_BITS)


with open("cipher1.bin", "wb") as f:
    f.write(cipher1)

with open("cipher2.bin", "wb") as f:
    f.write(cipher2)

print("cipher1 =", cipher1)
print("cipher2 =", cipher2)
