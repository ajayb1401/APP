from faster_whisper import WhisperModel
from Text_to_Translation import text_translate
model = WhisperModel("large-v2")
translator = text_translate
def audio_to_translate(input, target_language):
    seg = " "
    segments, info = model.transcribe(input)
    for segment in segments:
        seg += "%s " % (segment.text)
    translated_seg = translator(seg,target_language)
    return translated_seg