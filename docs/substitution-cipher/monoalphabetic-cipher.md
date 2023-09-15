# Monoalphabetic Cipher

The Monoalphabetic Cipher is a simple substitution cipher where each letter in the plaintext is replaced by a corresponding letter from a fixed **Substitution Alphabet (KEY)**.

The substitution is based on a one-to-one mapping between the letters of the plaintext alphabet and the letters of the substitution alphabet.

Unlike Cesar Cipher, in Monoalphabetic Cipher the key length in 26 Unique Characters giving a possibility of `26!` Keys.

## Encryption Process

1. **Choose a Substitution Alphabet (KEY)**: This alphabet will be used to replace the letters of the plaintext.
1. For each letter in the plaintext:
    - Find the position of the letter in the plaintext alphabet (A=0, B=1, ..., Z=25).
    - Replace the letter with the corresponding letter at the same position in the substitution alphabet.

### Encryption Formula:

`CipherText[i] = Key[ ALPHABETS.indexOf(PlainText[i]) ]`

**C = K[P]**

## Decryption Process

1. Use the same substitution alphabet that was used for encryption.
1. For each letter in the ciphertext:
    - Find the position of the letter in the substitution alphabet.
    - Replace the letter with the corresponding letter at the same position in the plaintext alphabet.

### Encryption Formula:

`Plaintext[i] = ALPHABETS[ Key.indexOf(CipherText[i]) ]`

**P = K[C]**

## Issue

Since every alphabet is Encrypted to the same set alphabet, in a Long enough Text, The key can be Determined.

Let's say **PlainText=`HELLO`** & **Cipher=`OLSSV`**. An attacker just need to look for a **'5 Letter Word that has 2 repeating Letters in the 3rd & 4th Position'**

So, Pattern matching is the biggest issue for Monoalphabetic Cipher.

## Algorithm Implementation

-   [C](../../algorithms/substitution-cipher/monoalphabetic-cipher/main.c)
