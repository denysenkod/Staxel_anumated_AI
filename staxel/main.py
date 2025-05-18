from elevenlabs import ElevenLabs
from tts_and_characters_with_timeline import save_base64_audio
from character_timeline_to_phonemes_timeline import text_to_phonemes_with_timeline
from phonemes_to_visemes import phonemes_to_viseme_timeline

def text_to_viseme_timeline(text):
    client = ElevenLabs(api_key="sk_524dca8b668b83f1dc910dcd0d239d415fc770f0ba6919ef")        
    res = client.text_to_speech.convert_with_timestamps(
	    voice_id="9BWtsMINqrJLrRacOk9x",
	    text=text
    )
    print(res.alignment)
    save_base64_audio(res.audio_base_64)
    phoneme_timeline = text_to_phonemes_with_timeline(res.alignment.characters, res.alignment.character_start_times_seconds, res.alignment.character_end_times_seconds)
    print(phoneme_timeline)
    print(phonemes_to_viseme_timeline(phoneme_timeline))

if __name__ == "__main__":
    text_to_viseme_timeline("Hi")

