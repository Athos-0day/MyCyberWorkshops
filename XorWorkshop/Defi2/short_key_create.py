# Clé en binaire 
KEY_BITS = [
    0b01001101,  
    0b01111001,  
    0b01001011,  
    0b01100101,  
    0b01111001   
]

# Flag 
FLAG_BITS = [
    0b01001110,  
    0b01100101,  
    0b01110100,  
    0b01111011,  
    0b01111000,  
    0b00110000,  
    0b01110010,  
    0b01011111,  
    0b00110001,  
    0b01110011,  
    0b01011111,  
    0b01101011,  
    0b00110011,   
    0b01111001,  
    0b01111101   
]

def xor_encrypt_bytes(plaintext_bits, key_bits):
    return bytes(
        plaintext_bits[i] ^ key_bits[i % len(key_bits)]
        for i in range(len(plaintext_bits))
    )

flag_cipher = xor_encrypt_bytes(FLAG_BITS,KEY_BITS)

with open("cipher.bin", "wb") as f:
    f.write(flag_cipher)

