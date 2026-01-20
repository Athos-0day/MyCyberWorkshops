# Lecture du flag chiffré
with open("cipher.bin", "rb") as f:
    cipher = f.read()

n = len(cipher)

# Hypothèse de flag
flag_guess = b"Net{" + b"x" * (n - 5) + b"}"

# XOR pour tester
test = bytes(
    cipher[i] ^ flag_guess[i]
    for i in range(n)
)

print("Résultat XOR :", test)

def xor_decrypt_bytes(plaintext_bits, key_bits):
    return bytes(
        plaintext_bits[i] ^ key_bits[i % len(key_bits)]
        for i in range(len(plaintext_bits))
    )

key = "MyKey"
key_bits = key.encode()

plaintext_flag = xor_decrypt_bytes(cipher,key_bits)

print(plaintext_flag)