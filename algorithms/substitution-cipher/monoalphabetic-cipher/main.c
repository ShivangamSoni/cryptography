#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

char ALPHABETS[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

enum Operation
{
    Encrypt,
    Decrypt
};

void flushInput();
void strToUppercase(char *str);
char *encrypt(char plaintext[], char key[]);
char *decrypt(char cipher[], char key[]);

int main()
{
    bool running = true;
    int opr;
    char key[27];

    do
    {
        printf("\n\nEncrypt(0) or Decrypt(1): ");
        scanf("%d", &opr);
        flushInput();

        if (opr != Decrypt && opr != Encrypt)
        {
            printf("Invalid Input!");
            continue;
        }

        printf("Enter the Key(26 Alphabets): ");
        fgets(key, 27, stdin);
        flushInput();
        strToUppercase(key);

        if (opr == Encrypt)
        {
            char plaintext[100];
            printf("Enter the Plaintext: ");
            fgets(plaintext, 100, stdin);

            char *cipher = encrypt(plaintext, key);

            printf("Plain Text: %s", plaintext);
            printf("Cipher Text: %s\n", cipher);
        }
        else
        {
            char cipher[100];
            printf("Enter the Cipher Text: ");
            fgets(cipher, 100, stdin);

            char *plaintext = decrypt(cipher, key);

            printf("Cipher Text: %s", cipher);
            printf("Plain Text: %s\n", plaintext);
        }

        printf("\n\nEnter Any Key to continue (Q to quit): ");
        char decision;
        scanf("%c", &decision);
        if (toupper(decision) == 'Q')
        {
            running = false;
        }
    } while (running);
    return 0;
}

void flushInput()
{
    while (getchar() != '\n')
        ;
}

void strToUppercase(char *str)
{
    int i = 0;
    while (str[i] != '\0')
    {
        str[i] = toupper(str[i]);
        i++;
    }
}

char *encrypt(char plaintext[], char key[])
{
    int i = 0;
    char *cipher = (char *)calloc(strlen(plaintext), sizeof(char));

    while (plaintext[i] != '\0')
    {
        if (isalpha(plaintext[i]))
        {
            char uppercase = toupper(plaintext[i]);
            int idx = strchr(ALPHABETS, uppercase) - ALPHABETS;
            char cipherChar = key[idx];
            cipher[i] = islower(plaintext[i]) ? tolower(cipherChar) : toupper(cipherChar);
        }
        else
        {
            cipher[i] = plaintext[i];
        }
        i++;
    }

    return cipher;
}

char *decrypt(char cipher[], char key[])
{
    int i = 0;
    char *plaintext = (char *)calloc(strlen(cipher), sizeof(char));

    while (cipher[i] != '\0')
    {
        if (isalpha(cipher[i]))
        {
            char uppercase = toupper(cipher[i]);
            int idx = strchr(key, uppercase) - key;
            char plainChar = ALPHABETS[idx];
            plaintext[i] = islower(cipher[i]) ? tolower(plainChar) : toupper(plainChar);
        }
        else
        {
            plaintext[i] = cipher[i];
        }
        i++;
    }

    return plaintext;
}
