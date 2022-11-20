import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi as yta

def process_text(text: str):
    if "=" in text:
        return text.split("=")[1]
    else:
        return text

st.write("## Extract Text from Youtube video \n ### POCS ML services")

link = st.text_input("Put the link here")


if link == "":
    st.write("enter the link")

else:
    st.write("#### working on extracting the text")
    video_id = (process_text(link))
    script = yta.get_transcript(video_id)
    extract_script = ""
    steps = 0
    batch_speech = ""
    for text in script:
        steps += 1
        extract_script += text["text"] + " "
        batch_speech += text["text"] + " "
        if steps % 10 == 0:
            st.write(batch_speech)
            batch_speech = ""

    #print(text["text"])

