import wave
import numpy as np
import simpleaudio as sa

def audioparser(file_path):
  with wave.open(file_path, 'rb') as wav_file:
    # Extract audio parameters
    params = wav_file.getparams()
    num_frames = wav_file.getnframes()
    audio_data = wav_file.readframes(num_frames)

  # Convert audio data to a NumPy array for manipulation
  audio_array = np.frombuffer(audio_data, dtype=np.int16)

  # Reduce volume (scale amplitude by a factor, e.g., 0.5 for 50% volume)
  volume_factor = 0.2  # Adjust this value to set the volume level
  adjusted_audio = (audio_array * volume_factor).astype(np.int16)

  # Convert back to bytes
  adjusted_audio_bytes = adjusted_audio.tobytes()

  return sa.WaveObject(adjusted_audio_bytes, params.nchannels, params.sampwidth, params.framerate)