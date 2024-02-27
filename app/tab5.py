from faster_whisper import WhisperModel
model=WhisperModel("large-v2")
final=[]
def  audio_streaming(input):
   seg=" "
   segments, info = model.transcribe((input))
   for segment in segments:
     seg +="%s" % (segment.text)
   final.append(seg)
   output_string = ' '.join(final)
   return output_string