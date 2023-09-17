ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    while True:
        key = input("Enter a Key: ").upper()
        plaintext = input("Enter a Plaintext: ").upper()

        key = cleanKey(key)
        keyMatrix = generateKeyMatrix(key)

        plaintext = generatePlaintextPairs(plaintext)

        cipher = encrypt(plaintext, keyMatrix)
        print(f"Cipher: {cipher}")

        decipher = decrypt(cipher, keyMatrix)
        print(f"Decipher: {decipher}")

        if input("\n\nPress Q/q to Exit: ").lower() == "q":
            print("Bye!!")
            break


def encrypt(plaintext: str, keyMatrix: list[str]) -> str:
    cipher = ""
    for i in range(0, len(plaintext), 2):
        c1 = plaintext[i]
        c2 = plaintext[i + 1]

        x1, y1 = indexOfInMatrix(keyMatrix, c1)
        x2, y2 = indexOfInMatrix(keyMatrix, c2)

        if x1 == x2:
            cipher += keyMatrix[x1][(y1 + 1) % 5]
            cipher += keyMatrix[x2][(y2 + 1) % 5]
        elif y1 == y2:
            cipher += keyMatrix[(x1 + 1) % 5][y1]
            cipher += keyMatrix[(x2 + 1) % 5][y2]
        else:
            cipher += keyMatrix[x1][y2]
            cipher += keyMatrix[x2][y1]

    return cipher


def decrypt(cipher: str, keyMatrix: list[str]) -> str:
    plaintext = ""
    for i in range(0, len(cipher), 2):
        c1 = cipher[i]
        c2 = cipher[i + 1]

        x1, y1 = indexOfInMatrix(keyMatrix, c1)
        x2, y2 = indexOfInMatrix(keyMatrix, c2)

        if x1 == x2:
            dc1 = keyMatrix[x1][(y1 - 1 + 5) % 5]
            dc2 = keyMatrix[x2][(y2 - 1 + 5) % 5]
        elif y1 == y2:
            dc1 = keyMatrix[(x1 - 1 + 5) % 5][y1]
            dc2 = keyMatrix[(x2 - 1 + 5) % 5][y2]
        else:
            dc1 = keyMatrix[x1][y2]
            dc2 = keyMatrix[x2][y1]

        if dc1 != "X":
            plaintext += dc1
        if dc2 != "X":
            plaintext += dc2

    return plaintext


def cleanKey(key: str) -> str:
    cKey = ""
    for c in key:
        if c == "J":
            c = "I"
        try:
            cKey.index(c)
        except ValueError:
            cKey += c
    return cKey


def generateKeyMatrix(key: str) -> list[str]:
    matrix = ["" for i in range(5)]
    i = 0
    for c in key:
        matrix[i] += c
        if len(matrix[i]) == 5:
            i += 1

    for c in ALPHABETS:
        if c != "J" and not isCharInMatrix(matrix, c):
            matrix[i] += c
            if len(matrix[i]) == 5:
                i += 1

    return matrix


def generatePlaintextPairs(plaintext: str) -> str:
    nPlaintext = ""
    plaintextLen = len(plaintext)
    i = 0
    while i < plaintextLen:
        c1 = plaintext[i]
        c2 = "X" if i == plaintextLen - 1 else plaintext[i + 1]
        if c1 == c2:
            c2 = "X"
            i += 1
        else:
            i += 2
        nPlaintext += c1 + c2

    return nPlaintext


def isCharInMatrix(matrix: list[str], char: str) -> bool:
    for row in matrix:
        for c in row:
            if c == char:
                return True
    return False


def indexOfInMatrix(matrix: list[str], char: str) -> tuple[int, int]:
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == char:
                return i, j
    return -1, -1


main()
