import string

# Generate a random key matrix
def generate_matrix():
    # Define the characters to be used in the matrix
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    # Sort the characters to ensure consistency
    characters = ''.join(sorted(characters))
    # Create a matrix with 10 characters per row
    matrix = [list(characters[i:i+10]) for i in range(0, len(characters), 10)]
    return matrix

# Encrypt text using the key matrix
def encrypt(text, key):
    encrypted_text = []
    for char in text:
        found = False
        # Iterate through the rows and columns of the key matrix
        for i in range(10):
            for j in range(10):
                if key[i][j] == char:
                    # Shift one position down within the same column
                    encrypted_char = key[(i + 1) % 10][j]
                    encrypted_text.append(encrypted_char)
                    found = True
                    break
            if found:
                break
        if not found:
            # If the character is not found in the matrix, append it as is
            encrypted_text.append(char)
    return ''.join(encrypted_text)

# Decrypt text using the key matrix
def decrypt(encrypted_text, key):
    decrypted_text = []
    for char in encrypted_text:
        found = False
        # Iterate through the rows and columns of the key matrix
        for i in range(10):
            for j in range(10):
                if key[i][j] == char:
                    # Shift one position up within the same column
                    decrypted_char = key[(i - 1) % 10][j]
                    decrypted_text.append(decrypted_char)
                    found = True
                    break
            if found:
                break
        if not found:
            # If the character is not found in the matrix, append it as is
            decrypted_text.append(char)
    return ''.join(decrypted_text)

# Example usage
text = "Hello, World!"
key = generate_matrix()

encrypted = encrypt(text, key)
decrypted = decrypt(encrypted, key)

# Print the original text, key matrix, encrypted text, and decrypted text
print("Original text:", text)
print("Key matrix:")
for row in key:
    print(' '.join(row))
print("Encrypted text:", encrypted)
print("Decrypted text:", decrypted)
