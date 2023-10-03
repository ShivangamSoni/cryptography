# Hill Cipher

Hill Cipher is a polygraphic substitution cipher that operates on groups of characters, making it more secure than traditional monoalphabetic ciphers like the Caesar Cipher. It uses linear algebra to perform its encryption and decryption processes.

## Key Verification

Before we delve into the encryption and decryption processes, let's understand the key verification process in Hill Cipher.

1. **Key Selection**: Choose a key matrix (K) that is square (dimensions are the same for both rows and columns) and invertible.

2. **Calculating the Inverse**: Calculate the modular multiplicative inverse of the determinant of the key matrix modulo the size of the alphabet you are working with. This inverse is used to find the modular multiplicative inverse of the determinant.

    ```
    If the determinant is 'd' and the size of the alphabet is 'm', find 'd_inv' such that (d * d_inv) % m = 1.
    ```

3. **Matrix Inversion**: Calculate the inverse of the key matrix modulo the size of the alphabet. This is done by finding the adjugate matrix and then multiplying it by the modular multiplicative inverse of the determinant.

    ```
    K_inv = (1 / d) * adjugate(K) % m
    ```

4. **Key Verification**: Ensure that the key matrix K is invertible. A matrix is invertible if and only if its determinant is non-zero and the modular multiplicative inverse of the determinant exists.

## Encryption Process

Now, let's walk through the encryption process using a plaintext message and the key matrix K.

1. **Key Preparation**: Convert the key matrix K and the plaintext message into numerical form, mapping each letter to its corresponding position in the alphabet (e.g., A=0, B=1, ..., Z=25).

2. **Message Padding**: If the length of the plaintext is not a multiple of the key matrix's dimension, pad the message with filler characters.

3. **Matrix Multiplication**: Divide the message into blocks equal to the dimension of the key matrix. Multiply each block by the key matrix K.

    ```
    Ciphertext_block = K * Plaintext_block % m
    ```

4. **Ciphertext Generation**: Convert the numerical results back to characters using the alphabet mapping. This generates the ciphertext.

## Decryption Process

Decryption in Hill Cipher is the reverse process of encryption and uses the inverse key matrix.

1. **Inverse Key**: Calculate the inverse of the key matrix K, which we derived during key verification.

2. **Matrix Multiplication**: Divide the ciphertext into blocks equal to the dimension of the key matrix. Multiply each block by the inverse key matrix K_inv.

    ```
    Plaintext_block = K_inv * Ciphertext_block % m
    ```

3. **Plaintext Generation**: Convert the numerical results back to characters using the alphabet mapping. This retrieves the original plaintext.

## Algorithm Implementation

-   [Python](../../../algorithms/substitution-cipher/polygraphic-cipher/hill-cipher/main.py)
