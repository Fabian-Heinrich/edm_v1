from pydub import AudioSegment
from pydub.generators import Sine
import pyttsx3

# Constants for the rhythm
bpm = 128  # typical BPM for EDM
beat_duration = 60000 // bpm  # duration of a beat in milliseconds (60,000 ms in a minute)
bar_duration = beat_duration * 4  # typical EDM bar has 4 beats

# Create a basic kick drum sound
kick = Sine(60).to_audio_segment(duration=150).fade_out(50)

# Create a bar with a kick on each beat
bar = AudioSegment.silent(duration=bar_duration)
for beat in range(4):
    bar = bar.overlay(kick, position=beat * beat_duration)

# Repeat the bar to create 8 bars
rhythm = bar * 8

# Export the rhythm to a file
file_path = "EDM_Rhythm.wav"
rhythm.export(file_path, format="wav")

# Generate speech using pyttsx3
engine = pyttsx3.init()
engine.save_to_file('Feel the beat, feel the heat, Moving under our feet. In the night, full of life, "Elektronische Tanz Musik" thrives.', 'speech.mp3')
engine.runAndWait()

# Load the speech and EDM track
speech = AudioSegment.from_file('speech.mp3')
edm_track = AudioSegment.from_file('EDM_Rhythm.wav')

# Combine the speech and EDM track
# You may need to adjust the volumes or overlay positions
combined = edm_track.overlay(speech, position=0)

# Export the combined audio
combined.export("combined_track.wav", format="wav")
