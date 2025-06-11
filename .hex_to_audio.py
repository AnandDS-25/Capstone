import base64
from gtts import gTTS

# Function to convert Base64 data from a file into speech and save as audio
def base64_to_audio(base64_file, output_audio):
    # Open the Base64 file in read mode
    with open(base64_file, 'r') as f:
        # Read the contents of the file and remove newlines
        base64_data = f.read().replace('\n', '')

    # Decode the Base64 data into text
    text = base64.b64decode(base64_data).decode('utf-8')

    # Print the extracted text for verification
    print(f'Text Extracted: {text}')

    # Convert text to speech using gTTS
    tts = gTTS(text, lang='en')

    # Save the generated speech as an audio file
    tts.save(output_audio)

    print(f'Audio file saved as {output_audio}')

# Example usage: Convert Base64 data from "decrypted_voice.b64" to an audio file "output_audio.mp3"
base64_to_audio("decrypted_voice.b64", "output_audio.mp3")
