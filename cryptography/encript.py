
# Encrypt text using the key matrix
from typing import List


def encrypt(text: str, key: List[List[str]]) -> str:
    encrypted_text = []
    for char in text:
        found = False
        # Iterate through the rows of the key matrix
        for row in key:
            if char in row:
                # Find the character in the row and get its index
                char_index = row.index(char)
                # Shift one position down within the same row
                encrypted_char = row[(char_index + 1) % len(row)]
                encrypted_text.append(encrypted_char)
                found = True
                break
        if not found:
            # If the character is not found in the matrix, append it as is
            encrypted_text.append(char)
    return ''.join(encrypted_text)
