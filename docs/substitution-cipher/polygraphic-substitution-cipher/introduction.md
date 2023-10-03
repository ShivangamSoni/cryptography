# Digraph Substitution Cipher

A digraph substitution cipher is a form of substitution cipher that replaces pairs of letters (digraphs) in the plaintext with other pairs of letters in the ciphertext.

This cipher operates on digraphs, which are combinations of two letters.

The primary goal is to obscure the relationship between individual letters in the plaintext, making it more difficult for attackers to decipher the message.

## Encryption:

-   Divide the plaintext into pairs of letters (digraphs). If the number of letters is odd, you can choose to add a filler character or ignore the unpaired letter.
-   Create a substitution key that specifies how each digraph in the plaintext will be replaced in the ciphertext.
-   For each digraph in the plaintext, find the corresponding digraph in the key and replace it.
-   Form the ciphertext by joining the replaced digraphs together.

## Decryption:

-   Divide the ciphertext into pairs of letters (digraphs).
-   Create the decryption key, which is the inverse of the encryption key. It specifies how each digraph in the ciphertext will be replaced to recover the original digraphs.
-   For each digraph in the ciphertext, find the corresponding digraph in the decryption key and replace it.
-   Form the plaintext by joining the replaced digraphs together.

## Security Considerations:

-   Digraph substitution ciphers are relatively weak compared to modern encryption methods because they operate on pairs of letters.
-   They are vulnerable to frequency analysis attacks, especially in languages where certain letter pairs are more common.
-   Digraph substitution ciphers are primarily used for educational purposes and not for securing sensitive information.

## Digraph Substitution Cipher Algorithms:

-   [Playfair Cipher](./playfair-cipher.md)
