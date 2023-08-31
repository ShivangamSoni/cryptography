# Cesar Cipher

The Caesar cipher is a **Monoalphabetic substitution cipher**.

The Caesar cipher works by shifting each letter in the plaintext by a fixed number of positions down or up the alphabet. This fixed shift is determined by the key, which is the number of positions each letter is shifted.

## Weakness of Cesar Cipher:

It's important to note that the Caesar cipher is relatively easy to break, even without a computer, using techniques like **brute force** or **frequency analysis**.

This is due to its simplicity and the limited number of possible keys (26, corresponding to the number of letters in the alphabet).

## Cesar Cipher Step-by-Step:

1. **Initial Setup**: Create a Table of Alphabets, each alphabet corresponding to a number starting from 0.

    |     |     |     |     |     |     |     |     |     |     |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | A   | B   | C   | D   | E   | F   | G   | H   | I   | J   |
    | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   |
    |     |     |     |     |     |     |     |     |     |     |
    | K   | L   | M   | N   | O   | P   | Q   | R   | S   | T   |
    | 10  | 11  | 12  | 13  | 14  | 15  | 16  | 17  | 18  | 19  |
    |     |     |     |     |     |     |     |     |     |     |
    | U   | V   | W   | X   | Y   | Z   |     |     |     |     |
    | 20  | 21  | 22  | 23  | 24  | 25  |     |     |     |     |

### Encryption:

1. Choose a Shift Key **(K)**
1. Separate the Plaintext into individual Characters
1. Find the Number for Each Plaintext Character **(P)** using the Table above
1. Add the Key to Plaintext Characters Index & wrap around

    **C = (P + K) % 26**

1. Concatenate the encrypted Characters.

### Decryption:

1. Choose a Shift Key **(K)**
1. Separate the Cipher Text into individual Characters
1. Find the Number for Each Cipher Text Character **(C)** using the Table above
1. Add the Key to Cipher Text Characters Index & wrap around

    **P = (C - K) % 26**

1. Concatenate the decrypted Characters.

## Issue

The problem with Cesar Cipher is that the Total Number of Possible Keys are 25 (1 to 25). Even when we select a key larger than that it gets normalized to bet between (1 to 25).

Hence, cracking a Cesar Cipher using **Brute Fore** is really easy.

## Algorithm Implementation

-   [C](../../algorithms/substitution-cipher/cesar-cipher/cesar-cipher.c)
