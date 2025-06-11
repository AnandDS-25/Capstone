import sounddevice as sd
import wave
import numpy as np
from faster_whisper import WhisperModel

# Settingst
FILENAME = "recorded_audio.wav"  # Output file name
TEXT_FILENAME = "transcription.txt"  # Transcription text file
HEX_FILENAME = "transcription.hex"  # Hex file output
SAMPLERATE = 44100  # Standard audio sample rate (Hz)
DURATION = 3 # Recording duration in seconds
CHANNELS = 1  # Mono audio #stream of audio info

print("🎤 Recording... Speak now!")

# Record audio
recorded_audio = sd.rec(int(SAMPLERATE * DURATION), samplerate=SAMPLERATE, channels=CHANNELS, dtype=np.int16)
sd.wait()  # Wait until recording is finished #formula tells us the no of samples.

# Save the audio as a WAV file3
with wave.open(FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(2)  # 16-bit audio #each sample is of two bytes
    wf.setframerate(SAMPLERATE)
    wf.writeframes(recorded_audio.tobytes())

print(f"✅ Recording saved as {FILENAME}")

# Load Faster-Whisper model with CPU optimization
print("🚀 Loading Faster-Whisper model...")
model = WhisperModel("medium", compute_type="int8")  # Use "tiny", "small", "medium", "large"#uses 8bit integers for computation
#model is an instance creates a whisper model 
# Transcribe the recorded audio
print("📝 Transcribing audio...")

segments, info = model.transcribe(FILENAME) #actual transcribing of the text takes place. from audio to text.
#info stroes additional deltails about transcriiption, like lang


# Collect transcription text
transcription_text = " ".join(segment.text for segment in segments)

# Save transcription to a text file
#just to check if the same text is recorded we do this conversion of text to byte(encoding)
with open(TEXT_FILENAME, "w", encoding="utf-8") as f:  #after encoding it stores into bytes but when opened we get string automatically decoded in py
    f.write(transcription_text)

print("\n✅ Transcription saved to transcription.txt")

# Convert the transcription text file to hex
with open(TEXT_FILENAME, "rb") as f:
    text_bytes = f.read() #converts bytes to string (decoding automatically)
    hex_data = text_bytes.hex()  # Convert to hex

# Save hex data to a file
with open(HEX_FILENAME, "w") as f:
    f.write(hex_data)

print(f"\n✅ Hex file generated: {HEX_FILENAME}")

