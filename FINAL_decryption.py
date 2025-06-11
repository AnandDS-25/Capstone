import binascii
import hashlib
from Crypto.Cipher import AES
from PIL import Image

# Function to extract a 256-bit AES key from an image
def get_key_from_image(image_path):
    img = Image.open(image_path).convert('RGB')
    pixels = list(img.getdata())
    key_data = bytes(sum(p) % 256 for p in pixels)[:32]  # Take 32 bytes
    return hashlib.sha256(key_data).digest()  # 256-bit key for AES

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
    decrypt_voice("hanu.bin", "key_image.jpg", "decrypted_voice.hex")
