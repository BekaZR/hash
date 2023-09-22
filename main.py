from cryptography import decrypt
from cryptography import encrypt
from service import generate_matrix

def user_interface_encrypt(key: list[list[str]], data: str) -> str:
    return encrypt(text=data, key=key)

def user_interface_decrypt(encrypted_data: str, key: list[list[str]]) -> str:
    return decrypt(encrypted_text=encrypted_data, key=key)

if __name__ == "__main__":
    key = generate_matrix(10)
    user_data = input("Enter your data to encrypt: ")
    
    # Encrypt user input
    user_encrypted_data = user_interface_encrypt(key=key, data=user_data)
    
    print("Encrypted text:", user_encrypted_data)
    
    # Provide instructions to the user
    print("\nTo decrypt the text, please enter the encrypted text and the key.")
    
    user_input_encrypted = input("Enter the encrypted text: ")
    
    # Decrypt user input
    decoded_data = user_interface_decrypt(encrypted_data=user_input_encrypted, key=key)
    
    print("\nDecrypted text:", decoded_data)
