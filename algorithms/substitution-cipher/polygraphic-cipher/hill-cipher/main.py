from math import modf


ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    while True:
        key = input("Enter a Key: ").upper()
        if not validateKeyLength(key):
            print("Key should create a n*n matrix")
            continue

        keyMatrix = generateKeyMatrix(key)
        determinant = calculateDeterminant(keyMatrix)
        determinantInverse = calculateDeterminantInverse(determinant)

        if determinantInverse == 0:
            print("Inverse is not Possible with the Given Key")
            continue

        keyMatrixInverse = calculateMatrixInverse(
            keyMatrix, determinantInverse)

        plaintext = input("Enter a Plaintext: ").upper()
        plaintextMatrices = generatePlaintextMatrices(
            plaintext, len(keyMatrix))

        cipher = encrypt(plaintextMatrices, keyMatrix)
        print(f"Cipher: {cipher}")

        cipherMatrices = generateCipherMatrices(cipher, len(keyMatrix))
        decipher = decrypt(cipherMatrices, keyMatrixInverse)
        print(f"Decipher: {decipher}")

        if input("\nEnter q/Q to Quit: ").lower() == 'q':
            print("Bye!")
            break


def encrypt(plaintextMatrices: list[list[int]], keyMatrix: list[list[int]]) -> str:
    cipherMatrices = []
    for row in plaintextMatrices:
        matrix = []
        for i in range(len(row)):
            j = 0
            cipher = 0
            while j < len(row):
                cipher += row[j] * keyMatrix[j][i]
                j += 1
            matrix.append(cipher % 26)
        cipherMatrices.append(matrix)
    return "".join([ALPHABETS[i] for row in cipherMatrices for i in row])


def decrypt(cipherMatrices: list[list[int]], keyMatrix: list[list[int]]) -> str:
    plaintextMatrices = []
    for row in cipherMatrices:
        matrix = []
        for i in range(len(row)):
            j = 0
            plaintext = 0
            while j < len(row):
                plaintext += row[j] * keyMatrix[j][i]
                j += 1
            matrix.append(plaintext % 26)
        plaintextMatrices.append(matrix)
    decipher = "".join([ALPHABETS[i]
                       for row in plaintextMatrices for i in row])
    return decipher[:-1] if decipher.endswith("X") else decipher


def generateKeyMatrix(key: str) -> list[list[int]]:
    n = int(len(key) ** 0.5)
    keyMatrix = [[] for _ in range(n)]
    i = 0
    for c in key:
        keyMatrix[i].append(ALPHABETS.index(c))
        if len(keyMatrix[i]) == n:
            i += 1
    return keyMatrix


def generatePlaintextMatrices(plaintext: str, n: int) -> list[list[int]]:
    matrices = []
    i = 0
    filler = ALPHABETS.index("X")
    while i < len(plaintext):
        matrix = []
        for _ in range(n):
            char = filler if i == len(
                plaintext) else ALPHABETS.index(plaintext[i])
            matrix.append(char)
            i += 1
        matrices.append(matrix)
    return matrices


def generateCipherMatrices(plaintext: str, n: int) -> list[list[int]]:
    matrices = []
    i = 0
    while i < len(plaintext):
        matrix = []
        for _ in range(n):
            char = ALPHABETS.index(plaintext[i])
            matrix.append(char)
            i += 1
        matrices.append(matrix)
    return matrices


def validateKeyLength(key: str) -> bool:
    return modf(len(key) ** 0.5)[0] == 0.0


def createSubMatrix(matrix: list[list[int]], rowSkip: int, colSkip: int) -> list[list[int]]:
    n = len(matrix) - 1
    subMatrix = [[] for _ in range(n)]
    k = 0
    for i in range(len(matrix)):
        if i == rowSkip:
            continue

        for j in range(len(matrix[0])):
            if j == colSkip:
                continue
            subMatrix[k].append(matrix[i][j])
        k += 1
    return subMatrix


def calculateDeterminant(matrix: list[list[int]]) -> int:
    d = 0
    row = matrix[0]
    for i, cell in enumerate(row):
        val = cell
        if len(row) != 1:
            val *= calculateDeterminant(createSubMatrix(matrix, 0, i))

        if i % 2 == 0:
            d += val
        else:
            d -= val

    if d < 0:
        while d < 0:
            d += 26

    return d


def calculateDeterminantInverse(d: int) -> int:
    if d % 2 != 0:
        i = 1
        while (d * i) % 26 != 1:
            i += 1
        return i
    return 0


def calculateAdjacentMatrix(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    adjMatrix = [[0] * n for _ in range(n)]
    pos = 0

    if n == 2:
        return [
            [matrix[1][1], -matrix[0][1]],
            [-matrix[1][0], matrix[0][0]]
        ]

    for i, row in enumerate(matrix):
        for j in range(len(row)):
            subMatrix = createSubMatrix(matrix, i, j)
            adjMatrix[j][i] = calculateDeterminant(subMatrix)

            if pos % 2 != 0:
                adjMatrix[j][i] = -adjMatrix[j][i]
            pos += 1

            adjMatrix[j][i] = adjMatrix[j][i] % 26

    return adjMatrix


def calculateMatrixInverse(matrix: list[list[int]], determinantInverse: int) -> list[list[int]]:
    adjMatrix = calculateAdjacentMatrix(matrix)
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            adjMatrix[i][j] *= determinantInverse

            if adjMatrix[i][j] < 0:
                temp = adjMatrix[i][j]
                while temp < 0:
                    temp += 26
                adjMatrix[i][j] = temp
            else:
                adjMatrix[i][j] %= 26
    return adjMatrix


def matrixToString(matrix: list[list[int]]) -> str:
    return "".join([ALPHABETS[i] for row in matrix for i in row])


main()
