#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

char ALPHA_MAP[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

enum Operation
{
    Encrypt,
    Decrypt
};

char *encrypt(char plaintext[], int key);
char *decrypt(char cipher[], int key);

int main()
{
    bool running = true;
    int opr;
    int key;

    do
    {
        printf("\n\nEncrypt(0) or Decrypt(1): ");
        scanf("%d", &opr);

        if (opr != Decrypt && opr != Encrypt)
        {
            printf("Invalid Input!");
            continue;
        }

        printf("Enter the Key: ");
        scanf("%d", &key);
        while (getchar() != '\n')
            ;

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

char *encrypt(char plaintext[], int key)
{
    int i = 0;
    char *cipher = (char *)calloc(strlen(plaintext), sizeof(char));
    while (plaintext[i] != '\0')
    {
        if (isalpha(plaintext[i]))
        {
            char uppercase = toupper(plaintext[i]);
            int idx = abs(strchr(ALPHA_MAP, uppercase) - ALPHA_MAP + key) % 26;
            cipher[i] = islower(plaintext[i]) ? tolower(ALPHA_MAP[idx]) : ALPHA_MAP[idx];
        }
        i++;
    }

    cipher[i] = '\0';
    return cipher;
}

char *decrypt(char cipher[], int key)
{
    int i = 0;
    char *plaintext = (char *)calloc(strlen(cipher), sizeof(char));
    while (cipher[i] != '\0')
    {
        if (isalpha(cipher[i]))
        {
            char uppercase = toupper(cipher[i]);
            int idx = abs(strchr(ALPHA_MAP, uppercase) - ALPHA_MAP - key) % 26;
            plaintext[i] = islower(cipher[i]) ? tolower(ALPHA_MAP[idx]) : ALPHA_MAP[idx];
        }
        i++;
    }

    plaintext[i] = '\0';
    return plaintext;
}