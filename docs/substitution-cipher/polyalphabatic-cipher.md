# Monoalphabetic Cipher

The Polyalphabetic Cipher is a Substitution Cipher where each letter in the plaintext can be replaced by multiple letters from a fixed **Keyword (KEY)**.

The KEY should be of the Length Less than or Equal to the PlainText Length.

Unlike Monoalphabetic Cipher, in Polyalphabetic Cipher a single letter can be replaced by multiple Letters hence, making it free from Pattern Matching which is a vulnerability of Monoalphabetic Cipher.

## Encryption Process

1. Choose a keyword. This keyword will determine the shifts for each letter in the plaintext.
1. For each letter in the plaintext:
    - Find the position of the corresponding letter in the keyword.
    - Shift the letter by the position value in the keyword's substitution alphabet.
    - Apply the modular operation to keep the result within the range of the alphabet (A=0, B=1, ..., Z=25).
    - Replace the letter with the shifted letter.

### Encryption Formula:

`CipherText[i] = ( PlainText[i] + Keyword[i % KeywordLen] ) % 26`

**C = (P + K) mod 26**

## Decryption Process

1. Use the same substitution alphabet that was used for encryption.
1. For each letter in the ciphertext:
    - Find the position of the letter in the substitution alphabet.
    - Replace the letter with the corresponding letter at the same position in the plaintext alphabet.

### Decryption Formula:

`PlainText[i] = ( CipherText[i] - Keyword[i % KeywordLen] + 26 ) % 26`

**P = (C - K + 26) mod 26**

## Algorithm Implementation

-   [C](../../algorithms/substitution-cipher/polyalphabetic-cipher/main.c)
-   [Python](../../algorithms/substitution-cipher/polyalphabetic-cipher/main.py)
