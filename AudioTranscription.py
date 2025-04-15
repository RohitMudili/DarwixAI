import whisper
import json
import torchaudio
from pyannote.audio import Pipeline
from datetime import timedelta

# ------------------- CONFIG -------------------
AUDIO_PATH = "your_audio_file.wav"  # or mp3
HUGGINGFACE_TOKEN = "YOUR_HF_TOKEN_HERE"
MODEL_SIZE = "medium"  # can be base, small, medium, large
# ----------------------------------------------

# Load Whisper model
print("Loading Whisper model...")
whisper_model = whisper.load_model(MODEL_SIZE)
transcription = whisper_model.transcribe(AUDIO_PATH, verbose=True)

# Load diarization pipeline
print("Loading pyannote diarization pipeline...")
diarization_pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization",
    use_auth_token=HUGGINGFACE_TOKEN
)

# Run diarization
print("Running speaker diarization...")
diarization_result = diarization_pipeline(AUDIO_PATH)

# Function to find which speaker spoke in each whisper segment
def get_speaker_segments(diarization, segments):
    speaker_data = []

    for segment in segments:
        seg_start = segment['start']
        seg_end = segment['end']
        seg_text = segment['text']

        speaker_label = "Unknown"

        for turn, _, speaker in diarization.itertracks(yield_label=True):
            if turn.start <= seg_start <= turn.end or turn.start <= seg_end <= turn.end:
                speaker_label = speaker
                break

        speaker_data.append({
            "speaker": speaker_label,
            "start": round(seg_start, 2),
            "end": round(seg_end, 2),
            "text": seg_text.strip()
        })

    return speaker_data

# Match speakers to transcribed segments
print("Aligning transcriptions with speakers...")
final_output = get_speaker_segments(diarization_result, transcription["segments"])

# Save output as JSON
with open("transcription_with_speakers.json", "w", encoding="utf-8") as f:
    json.dump(final_output, f, indent=2, ensure_ascii=False)

# Print results
print("\nTranscription with Speaker Labels:")
for entry in final_output:
    start = str(timedelta(seconds=entry["start"]))
    end = str(timedelta(seconds=entry["end"]))
    print(f"[{start} - {end}] {entry['speaker']}: {entry['text']}")
