ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    while True:
        key = input("Enter a Key (26 Distinct Characters): ").upper()
        if len("".join(set(key))) != 26:
            print("\n\tKey Must be 26 Distinct Characters\n")
            continue

        plaintext = input("Enter a Plaintext: ")
        cipher = encrypt(key, plaintext)
        print(f"Cipher: {cipher}")
        print(f"Decipher: {decrypt(key, cipher)}")

        if input("\n\nPress Q/q to Exit: ").lower() == "q":
            print("Bye!!")
            break


def encrypt(key: str, plaintext: str) -> str:
    cipher = ""
    for c in plaintext:
        if c.isalpha():
            pIdx = ALPHABETS.index(c.upper())
            cChar = key[pIdx]
            cipher += cChar if c.isupper() else cChar.lower()
        else:
            cipher += c
    return cipher


def decrypt(key: str, cipher: str) -> str:
    plaintext = ""
    for c in cipher:
        if c.isalpha():
            cIdx = key.index(c.upper())
            pChar = ALPHABETS[cIdx]
            plaintext += pChar if c.isupper() else pChar.lower()
        else:
            plaintext += c
    return plaintext


main()
