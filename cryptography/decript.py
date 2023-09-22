# Decrypt text using the key matrix
from typing import List


def decrypt(encrypted_text: str, key: List[List[str]]) -> str:
    decrypted_text = []
    for char in encrypted_text:
        found = False
        # Iterate through the rows of the key matrix
        for row in key:
            if char in row:
                # Find the character in the row and get its index
                char_index = row.index(char)
                # Shift one position up within the same row
                decrypted_char = row[(char_index - 1) % len(row)]
                decrypted_text.append(decrypted_char)
                found = True
                break
        if not found:
            # If the character is not found in the matrix, append it as is
            decrypted_text.append(char)
    return ''.join(decrypted_text)
