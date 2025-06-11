import binascii
import hashlib
from Crypto.Cipher import AES
from PIL import Image

# Function to extract a 256-bit AES key from an image
def get_key_from_image(image_path):
    img = Image.open(image_path).convert('RGB')
    pixels = list(img.getdata())

    # Generate a key from pixel values (hashing ensures a fixed-length key)
    key_data = bytes(sum(p) % 256 for p in pixels)[:32]  # Take 32 bytes
    return hashlib.sha256(key_data).digest()  # 256-bit key for AES

# Function to encrypt a voice hex file using an image as a key
def encrypt_voice(hex_file, image_key_path, output_file):
    key = get_key_from_image(image_key_path)
    iv = b'This is an IV456'  # 16-byte IV (Change for security)

    # Read the hex file and convert to bytes
    with open(hex_file, 'rb') as f:
        voice_data = binascii.unhexlify(f.read().strip())  # Convert hex to bytes

    # Ensure the data is a multiple of 16 bytes (AES block size)
    while len(voice_data) % 16 != 0:
        voice_data += b'\x00'

    # Encrypt the voice data using AES CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(voice_data)

    # Save the encrypted data
    with open(output_file, 'wb') as f:
        f.write(encrypted_data)

    print(f"✅ Voice encryption complete. Encrypted file saved as: {output_file}")

# Function to decrypt a voice file using an image as a key
def decrypt_voice(encrypted_file, image_key_path, output_file):
    key = get_key_from_image(image_key_path)
    iv = b'This is an IV456'

    # Read the encrypted file
    with open(encrypted_file, 'rb') as f:
        encrypted_data = f.read()

    # Decrypt the data
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_data).rstrip(b'\x00')  # Remove padding

    # Save the decrypted data back to hex format
    with open(output_file, 'wb') as f:
        f.write(binascii.hexlify(decrypted_data))

    print(f"✅ Voice decryption complete. Decrypted file saved as: {output_file}")

# Example usage
if __name__ == "__main__":
    encrypt_voice("transcription.hex", "key_image.jpg", "encrypted_voice.bin")
    decrypt_voice("encrypted_voice.bin", "key_image.jpg", "decrypted_voice.hex")
