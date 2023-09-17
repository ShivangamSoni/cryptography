# Playfair Cipher

The Playfair cipher encrypts plaintext by substituting pairs of letters (digraphs) with other digraphs based on a key.

It uses a 5x5 matrix (usually called a Playfair square) to represent the key.

Each letter in the matrix is unique, and one letter of the alphabet (usually 'J') is omitted to accommodate 26 letters.

## Key Preparation

-   Choose a Key
-   Remove any duplicate letters
-   Remove the letter **J**

## Cipher Matrix

-   Create a **5x5 Matrix**.
-   Fill the matrix with letters from the **KEY**.
-   Fill the remaining spaces with Alphabets, starting from 'A' to 'Z'. Skipping the Letters that already exist.

## Plaintext Preparation

-   Break the plaintext into digraphs of two letter pairs.
-   If the digraph consists of same letter, insert **'X'** between them
-   If the number of letters is odd, add **'X'** at the end to complete the last digraph

## Encryption

-   If two letters are in the same row, replace each letter with the letter to it's right, cyclically i.e., if the letter we are encrypting if at the end of the row then it will replaced by the letter at the starting of the row as if it were connected like a circular structure.
-   If two letters are in the same column, replace each letter with the letter below it, cyclically.
-   If the two letters are neither in the same row nor the same column, form a rectangle with them and replace each letter with the letter on the same row but in the column of the other letter (so, at the intersection point).

## Decryption

-   Break the cipher into digraphs
-   If two letters are in the same row, replace each letter with the letter to it's left, cyclically.
-   If two letters are in the same column, replace each letter with the letter above it, cyclically.
-   If the two letters are neither in the same row nor the same column, form a rectangle with them and replace each letter with the letter on the same row but in the column of the other letter (so, at the intersection point).

## Algorithm Implementation

-   [C](../../../algorithms/substitution-cipher/digraph-substitution-cipher/playfair-cipher/main.c)
-   [Python](../../../algorithms/substitution-cipher/digraph-substitution-cipher/playfair-cipher/main.py)
