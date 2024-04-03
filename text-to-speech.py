import streamlit as st
from gtts import gTTS

def text_to_speech_gtts(text):
    tts = gTTS(text)
    tts.save("output.mp3")
    st.audio("output.mp3", format="audio/mp3")



def main():
    st.title("Text to Speech App")
    text = st.text_area("Enter the text you want to convert to speech:")
    engine_choice = st.radio("Choose TTS Engine:", ("gtts", "pyttsx3"))

    if st.button("Convert to Speech"):
        if engine_choice == "gtts":
            text_to_speech_gtts(text)

if __name__ == "__main__":
    main()
