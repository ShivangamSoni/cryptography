ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    while True:
        plaintext = input("Enter a Plaintext: ")
        key = input("Enter a Key: ").upper()

        cipher = encrypt(key, plaintext)
        print(f"Cipher: {cipher}")
        print(f"Decipher: {decrypt(key, cipher)}")

        if input("\n\nPress Q/q to Exit: ").lower() == "q":
            print("Bye!!")
            break


def encrypt(key: str, plaintext: str) -> str:
    cipher = ""
    for i, c in enumerate(plaintext):
        if c.isalpha():
            idxP = ALPHABETS.index(c.upper())
            kChar = key[i % len(key)]
            idxK = ALPHABETS.index(kChar)
            idxC = (idxP + idxK) % 26
            cChar = ALPHABETS[idxC]
            cipher += cChar if c.isupper() else cChar.lower()
        else:
            cipher += c
    return cipher


def decrypt(key: str, cipher: str) -> str:
    plaintext = ""
    for i, c in enumerate(cipher):
        if c.isalpha():
            idxC = ALPHABETS.index(c.upper())
            kChar = key[i % len(key)]
            idxK = ALPHABETS.index(kChar)
            idxP = (idxC - idxK + 26) % 26
            pChar = ALPHABETS[idxP]
            plaintext += pChar if c.isupper() else pChar.lower()
        else:
            plaintext += c
    return plaintext


main()
