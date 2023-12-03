import wave

def convert_audio_bytes_to_wav(audio_bytes, output_path):
    with wave.open(output_path, 'wb') as wav_file:
        # Set the WAV file's parameters
        wav_file.setframerate(44100)  # 44.1 kHz sample rate
        wav_file.setnchannels(2)  # Stereo audio
        wav_file.setsampwidth(2)  # 16-bit audio

        # Write the audio bytes to the WAV file
        wav_file.writeframes(audio_bytes)