import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Home", page_icon="🏡", layout="wide")

image_path2 = Path("/mount/src/talk-to-files/srcs/logo.png").with_name("favi.png")
image_path = Path("/mount/src/talk-to-files/srcs/logo.png").with_name("logo.png")
st.sidebar.image(str(image_path), width=170)

st.title('Talk to your Files! 🚀')

st.write('Sebastian Carmona  -  Data Scientist  - Version 1.0')

st.write('On the following app you can upload a file and talk to it.')

st.write('''
        There are two tabs depending on the file type you want to upload, and what you want to do with it.
         \n
         1. If it is a PDF file, just click on the PDF tab and you will be able to ask questions to the file and get answers.
         \n
         2. If it is a CSV file, just click on the CSV tab and you will be able to ask questions to the file and get answers, or generate a quick EDA from the CSV file.
         ''')

st.write("If you want to know more about the project or me, please visit the GitHub repository or my LinkedIn profile.")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image('https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fbeaconman.com%2Fwp-content%2Fuploads%2F2020%2F11%2FLinkedin_symbol_transparent.png&f=1&nofb=1&ipt=4796ff1975a7a198f5c6dc48c204d6fcffa773a0c3a269d3fb960d9ea94323bd&ipo=images', caption='', width=70)
    st.markdown(f"[Linkedin](https://www.linkedin.com/in/sebascarmona)", unsafe_allow_html=True)


with col2:
    st.image('https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpluspng.com%2Fimg-png%2Fgithub-logo-png-github-logos-and-usage-github-800x665.png&f=1&nofb=1&ipt=bd79ac2097ce60e64378c291855a5374e4a91c5c77cfe01dc27f02380b5619f2&ipo=images', caption='', width=70)
    st.markdown(f"[Github](https://github.com/Sebasc322)", unsafe_allow_html=True)

with col3:
    st.image('https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.underconsideration.com%2Fbrandnew%2Farchives%2Fmedium_2017_monogram.png&f=1&nofb=1&ipt=966d53db79baf267aa2763fef5d0a01aca415869c243101633d1ca6223c1006f&ipo=images', caption='', width=70)
    st.markdown(f"[Medium](https://sebascar322.medium.com/)", unsafe_allow_html=True)

with col4:
    st.image(str(image_path2), caption='', width=70)
    st.markdown(f"[Portfolio](https://www.sebascarmona.com/)", unsafe_allow_html=True)
