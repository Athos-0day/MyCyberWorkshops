# Récupération des deux textes chiffrés en binaire
with open("cipher1.bin", "rb") as f:
    cipher1 = f.read()

with open("cipher2.bin", "rb") as f:
    cipher2 = f.read()

# XOR des deux messages
xor_result = bytes(a ^ b for a, b in zip(cipher1, cipher2))

print("C1 ⊕ C2 =", xor_result)


def crib_drag(xor_bytes, crib):
    crib = crib.encode()
    results = []

    for i in range(len(xor_bytes) - len(crib) + 1):
        segment = xor_bytes[i:i+len(crib)]
        guess = bytes(a ^ b for a, b in zip(segment, crib))

        if all(32 <= c <= 126 for c in guess):
            results.append((i, guess.decode()))

    return results


results = crib_drag(xor_result, "Net7")

for pos, text in results:
    print(f"Position {pos}: {text}")

known_plain = b"Net7"
pos = 0  # Net7 commence à l’indice 0

m2_part = bytes(
    xor_result[pos+i] ^ known_plain[i]
    for i in range(len(known_plain))
)

print("M2 =", m2_part.decode())

