ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    while True:
        try:
            key = int(input("Enter a Key (Number): "))
        except ValueError:
            print("\tInvalid Input\n")
            continue

        plaintext = input("Enter a Plaintext: ")
        cipher = encrypt(key, plaintext)
        print(f"Cipher: {cipher}")
        print(f"Decipher: {decrypt(key, cipher)}")

        if input("\n\nPress Q/q to Exit: ").lower() == "q":
            print("Bye!!")
            break


def encrypt(key: int, plaintext: str) -> str:
    cipher = ""
    for c in plaintext:
        if c.isalpha():
            pIdx = ALPHABETS.index(c.upper())
            cChar = ALPHABETS[(pIdx + key) % 26]
            cipher += cChar.lower() if c.islower() else cChar
        else:
            cipher += c
    return cipher


def decrypt(key: int, cipher: str) -> str:
    plaintext = ""
    for c in cipher:
        if c.isalpha():
            cIdx = ALPHABETS.index(c.upper())
            pIdx = cIdx - key
            if pIdx < 0:
                if abs(pIdx) <= 26:
                    pIdx += 26
                else:
                    tmp = 26
                    while (tmp < abs(pIdx)):
                        tmp += 26
                    pIdx += tmp
            pChar = ALPHABETS[pIdx]
            plaintext += pChar.lower() if c.islower() else pChar
        else:
            plaintext += c
    return plaintext


main()
