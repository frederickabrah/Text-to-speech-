from gtts import gTTS
import os

# Ask user to input text
text = input("Enter the text you want to convert to audio: ")

# Create gTTS object
tts = gTTS(text)

# Save audio file
audio_file = "output.mp3"
tts.save(audio_file)

# Play audio file
os.system("start " + audio_file)  # For Windows
# os.system("afplay " + audio_file)  # For macOS
# os.system("mpg123 " + audio_file)  # For Linux

print("Audio file saved and played successfully.")
