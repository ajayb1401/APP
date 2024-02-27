import gradio as gr
from tab1 import audio_to_translate
from tab2 import video_translate
from tab3 import text_translate
from tab4 import microphone_to_translation
from tab5 import audio_streaming

languages = {
    "Afrikaans": "af", "Amharic": "am", "Arabic": "ar", "Asturian": "ast", "Azerbaijani": "az",
    "Bashkir": "ba", "Belarusian": "be", "Bulgarian": "bg", "Bengali": "bn", "Breton": "br",
    "Bosnian": "bs", "Catalan": "ca", "Cebuano": "ceb", "Czech": "cs", "Welsh": "cy",
    "Danish": "da", "German": "de", "Greeek": "el", "English": "en", "Spanish": "es", "Estonian": "et",
    "Persian": "fa", "Fulah": "ff", "Finnish": "fi", "French": "fr", "Western Frisian": "fy", "Irish": "ga",
    "Gaelic": "gd", "Galician": "gl", "Gujarati": "gu", "Hausa": "ha", "Hebrew": "he", "Hindi": "hi",
    "Croatian": "hr", "Haitian": "ht", "Hungarian": "hu", "Armenian": "hy", "Indonesian": "id", "Igbo": "ig",
    "Iloko": "ilo", "Icelandic": "is", "Italian": "it", "Japanese": "ja", "Javanese": "jv", "Georgian": "ka",
    "Kazakh": "kk", "Central Khmer": "km", "Kannada": "kn", "Korean": "ko", "Luxembourgish": "lb", "Ganda": "lg",
    "Lingala": "ln", "Lao": "lo", "Lithuanian": "lt", "Latvian": "lv", "Malagasy": "mg", "Macedonian": "mk",
    "Malayalam": "ml", "Mongolian": "mn", "Marathi": "mr", "Malay": "ms", "Burmese": "my", "Nepali": "ne",
    "Dutch": "nl", "Norwegian": "no", "Northern Sotho": "ns", "Occitan": "oc", "Oriya": "or",
    "Panjabi": "pa", "Polish": "pl", "Pushto": "ps", "Portuguese": "pt", "Romanian": "ro",
    "Russian": "ru", "Sindhi": "sd", "Sinhala": "si", "Slovak": "sk", "Slovenian": "sl", "Somali": "so",
    "Albanian": "sq", "Serbian": "sr", "Swati": "ss", "Sundanese": "su", "Swedish": "sv", "Swahili": "sw",
    "Tamil": "ta", "Thai": "th", "Tagalog": "tl", "Tswana": "tn", "Turkish": "tr", "Ukrainian": "uk",
    "Urdu": "ur", "Uzbek": "uz", "Vietnamese": "vi", "Wolof": "wo", "Xhosa": "xh", "Yiddish": "yi",
    "Yoruba": "yo", "Chinese": "zh", "Zulu": "zu"
}



def audio_text(audio_file, target_language):
    target_language_name = list(languages.values())[list(languages.keys()).index(target_language)]
    return audio_to_translate(audio_file, target_language_name)
def video_translation(videofile,target_lang):
    target_language_name = list(languages.values())[list(languages.keys()).index(target_lang)]
    return video_translate(videofile,target_language_name)
def text_translation(text,targetlang):
    target_language_name = list(languages.values())[list(languages.keys()).index(targetlang)]
    return text_translate(text,target_language_name)
def microphone_text(audio,targetlang):
    target_language_name = list(languages.values())[list(languages.keys()).index(targetlang)]
    return microphone_to_translation(audio,target_language_name)
def microphone_live(audio):
    return audio_streaming(audio)

with gr.Blocks() as trail:
   with gr.Tab("audio to translation"):
        audio_input = [gr.Audio(label="Speak Here",type="filepath"),
               gr.Dropdown(label="Target Language", choices=list(languages.keys()))]
        text_output = gr.Textbox(label="Transcription")
        gr.Interface(
            fn=audio_text,
            inputs=audio_input,
            outputs=text_output,
            examples=[["sam1.mp3"],
                      ["sam2.mp3"]],
            title="Audio to text Translator",
            allow_flagging=False
        )
   with gr.Tab("video to translation"):
    video_input = [gr.Video(label="Put your video here"),
               gr.Dropdown(label="Target Language", choices=list(languages.keys()))]
    text_output = gr.Textbox(label="Transcription")
    gr.Interface(
                fn=video_translation,
                inputs=video_input,
                outputs=text_output,
                examples=[["sam1.mp4"],
                          ["sam2.mp4"],
                          ["sam3.mp4"]],
                title="video-to-Text Translator",
                allow_flagging=False
            )
   with gr.Tab("text to translation"):
    audio_input = [gr.Text(label="Enter your text here"),
               gr.Dropdown(label="Target Language", choices=list(languages.keys()))]
    text_output = gr.Textbox(label="Transcription")
    gr.Interface(
                fn=text_translation,
                inputs=audio_input,
                outputs=text_output,
                examples=[["He is good boy"],
                          ["This is my New home"],
                          ["I Love my Puppy"]],
                title="Text to Translation",
                description="Enter the text to Translate.",
                allow_flagging=False
            )
   with gr.Tab("microphone to translation"):
    inputs=[gr.Audio(sources="microphone",type="filepath"),
                gr.Dropdown(label="Target Language", choices=list(languages.keys()))]
    text_output = gr.Textbox(label="Transcription")
    gr.Interface(
                fn=microphone_text,
                inputs=inputs,
                outputs=text_output,
                title="Speech-to-Text Converter",
                description="Speak into the microphone and get text Translation.",
                allow_flagging=False
        )
   with gr.Tab("Microphone to Streaming Transcription"):
    audio_input=[gr.Audio(streaming=True,type="filepath")]
    text_output = gr.Textbox(label="Transcription")
    gr.Interface(
                fn=microphone_live,
                inputs=audio_input,
                outputs=text_output,
                title="Speech-to-Text Converter",
                description="Speak into the microphone and get text Transcription.",
                allow_flagging=False,
                live="true"
        )
trail.launch()