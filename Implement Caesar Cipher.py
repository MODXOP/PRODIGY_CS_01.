def encrypt(text, shift):
    """Encrypt the text using the Caesar cipher."""
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    """Decrypt the text using the Caesar cipher."""
    return encrypt(text, -shift)

def main():
    while True:
        operation = input("Do you want to (e)ncrypt or (d)ecrypt a message? (e/d): ").strip().lower() 
        if operation in ('e', 'd'):
            message = input("Enter the message: ").strip()
            shift = int(input("Enter the shift value: ").strip())
            
            if operation == 'e':
                result = encrypt(message, shift)
                print(f"Encrypted message: {result}")
            elif operation == 'd':
                result = decrypt(message, shift)
                print(f"Decrypted message: {result}")
        else:
            print("Invalid operation. Please choose 'e' for encryption or 'd' for decryption.")

        again = input("Do you want to perform another operation? (y/n): ").strip().lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()