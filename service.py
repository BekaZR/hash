import string
import random
from typing import List

# Generate a random key matrix with a specified number of characters per row
def generate_matrix(characters_per_row: int) -> List[List[str]]:
    # Define all characters that can be present in the input text
    all_characters = string.ascii_letters + string.digits + string.punctuation + ' ' + 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    
    # Shuffle the characters randomly to create a key matrix
    shuffled_characters = list(all_characters)
    random.shuffle(shuffled_characters)
    
    # Create a matrix with 10 characters per row
    matrix = [shuffled_characters[i:i+characters_per_row] for i in range(0, len(shuffled_characters), 10)]
    return matrix
