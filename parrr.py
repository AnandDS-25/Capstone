import serial
import time

# Serial port for sender Arduino (Change COM5 if needed)
SERIAL_PORT = "COM5"
BAUD_RATE = 115200
FILE_PATH = "encrypted_voice.bin"  # Path to your encrypted .bin file

def send_file():
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)  # Allow Arduino to reset
        print(f"Connected to {SERIAL_PORT}, sending {FILE_PATH}...")

        with open(FILE_PATH, "rb") as file:
            while chunk := file.read(32):  # Read 32-byte chunks
                ser.write(chunk)  # Send to Arduino
                time.sleep(0.05)  # Delay for stability
                print(f"Sent {len(chunk)} bytes")

        print("File transmission complete.")
        ser.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_file()