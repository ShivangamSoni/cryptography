#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

char ALPHABETS[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

char *encrypt(char *plaintext, char **matrix);
char *decrypt(char *cipher, char **matrix);
char *cleanKey(char *key);
char **generateMatrix(char *key);
char *createPlaintextPairs(char *plaintext);
int *charInMatrix(char **matrix, char c, int rows, int cols);
bool isCharInMatrix(char **matrix, char c, int rows, int cols);

// Utility Functions
int strlen(char *str);
int indexOf(char *str, char c);

int main()
{
    char plaintext[101];
    char key[27];

    printf("Enter a Key: ");
    fgets(key, 27, stdin);

    printf("Enter a Plaintext: ");
    fgets(plaintext, 101, stdin);

    char *cKey = cleanKey(key);
    char **matrix = generateMatrix(cKey);

    // Encrypt
    char *nPlaintext = createPlaintextPairs(plaintext);
    char *cipher = encrypt(nPlaintext, matrix);
    printf("\nCipher: %s", cipher);

    // Decrypt
    char *decipher = decrypt(cipher, matrix);
    printf("\nDecipher: %s", decipher);

    return 0;
}

char *encrypt(char *plaintext, char **matrix)
{
    int len = strlen(plaintext);
    char *cipher = (char *)calloc(len, sizeof(char));
    for (int i = 0, j = 0; i < len; i += 2, j += 2)
    {
        char c1 = plaintext[i];
        char c2 = plaintext[i + 1];

        int *idx1 = charInMatrix(matrix, c1, 5, 5);
        int *idx2 = charInMatrix(matrix, c2, 5, 5);

        if (idx1[0] == idx2[0])
        {
            cipher[j] = matrix[idx1[0]][(idx1[1] + 1) % 5];
            cipher[j + 1] = matrix[idx2[0]][(idx2[1] + 1) % 5];
        }
        else if (idx1[1] == idx2[1])
        {
            cipher[j] = matrix[(idx1[0] + 1) % 5][idx1[1]];
            cipher[j + 1] = matrix[(idx2[0] + 1) % 5][idx2[1]];
        }
        else
        {
            cipher[j] = matrix[idx1[0]][idx2[1]];
            cipher[j + 1] = matrix[idx2[0]][idx1[1]];
        }
    }
    return cipher;
}

char *decrypt(char *cipher, char **matrix)
{
    int len = strlen(cipher);
    char *plaintext = (char *)calloc(len, sizeof(char));
    for (int i = 0, j = 0; i < len; i += 2)
    {
        char c1 = cipher[i];
        char c2 = cipher[i + 1];

        int *idx1 = charInMatrix(matrix, c1, 5, 5);
        int *idx2 = charInMatrix(matrix, c2, 5, 5);

        char ch1;
        char ch2;

        if (idx1[0] == idx2[0])
        {
            ch1 = matrix[idx1[0]][(idx1[1] - 1 + 5) % 5];
            ch2 = matrix[idx2[0]][(idx2[1] - 1 + 5) % 5];
        }
        else if (idx1[1] == idx2[1])
        {
            ch1 = matrix[(idx1[0] - 1 + 5) % 5][idx1[1]];
            ch2 = matrix[(idx2[0] - 1 + 5) % 5][idx2[1]];
        }
        else
        {
            ch1 = matrix[idx1[0]][idx2[1]];
            ch2 = matrix[idx2[0]][idx1[1]];
        }

        if (ch1 != 'X')
        {
            plaintext[j] = ch1;
            j++;
        }

        if (ch2 != 'X')
        {
            plaintext[j] = ch2;
            j++;
        }
    }
    return plaintext;
}

char *cleanKey(char *key)
{
    char *nKey = (char *)calloc(strlen(key), sizeof(char));
    int i = 0, j = 0;
    while (key[i] != '\0')
    {
        char c = key[i];
        if (c == 'J')
        {
            c = 'I';
        }

        int currIdx = indexOf(nKey, c);
        if (currIdx == -1)
        {
            nKey[j] = c;
            j++;
        }
        i++;
    }
    return nKey;
}

char **generateMatrix(char *key)
{
    char **matrix = (char **)malloc(5 * sizeof(char *));
    for (int i = 0; i < 5; i++)
    {
        matrix[i] = (char *)malloc(6 * sizeof(char));
    }

    int keyLen = strlen(key);
    int j = 0, k = 0;
    for (int i = 0; i < keyLen; i++)
    {
        matrix[j][k] = key[i];
        k++;

        if (k >= 5)
        {
            matrix[j][k] = '\0';
            k = k % 5;
            j++;
        }
    }

    int i = 0;
    while (j < 5)
    {
        if (ALPHABETS[i] != 'J' && !isCharInMatrix(matrix, ALPHABETS[i], 5, 5))
        {
            matrix[j][k] = ALPHABETS[i];
            k++;

            if (k >= 5)
            {
                matrix[j][k] = '\0';
                k = k % 5;
                j++;
            }
        }
        i++;
    }

    return matrix;
}
char *createPlaintextPairs(char *plaintext)
{
    int plainLen = strlen(plaintext);
    char *nPlaintext = (char *)calloc(plainLen + 10, sizeof(char));
    int k = 0;
    for (int i = 0; i < plainLen;)
    {
        char c1 = plaintext[i];
        char c2 = plaintext[i + 1];

        if (c1 == c2 || i == plainLen - 1)
        {
            c2 = 'X';
            i++;
        }
        else
        {
            i += 2;
        }

        nPlaintext[k] = c1;
        nPlaintext[k + 1] = c2;
        k += 2;
    }
    nPlaintext[k] = '\0';
    return nPlaintext;
}

int *charInMatrix(char **matrix, char c, int rows, int cols)
{
    int *res = (int *)calloc(2, sizeof(int));
    res[0] = -1;
    res[1] = -1;

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            if (matrix[i][j] == c)
            {
                res[0] = i;
                res[1] = j;
                break;
            }
        }
    }

    return res;
}

bool isCharInMatrix(char **matrix, char c, int rows, int cols)
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            if (matrix[i][j] == c)
            {
                return true;
            }
        }
    }
    return false;
}

// Utilities
int strlen(char *str)
{
    int i = 0;
    while (str[i] != '\0')
    {
        i++;
    }
    return i - 1;
}

int indexOf(char *str, char c)
{
    int i = 0;
    while (str[i] != '\0')
    {
        if (str[i] == c)
        {
            return i;
        }
        i++;
    }
    return -1;
}
