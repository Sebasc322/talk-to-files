import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏡", layout="wide")

icon_path = 'https://lh5.googleusercontent.com/dovsuxe_56wOzr-ZCWqJAakP8K4GYl73alTFb_NTAr7UjwUNUdjK54cRoc8lAecqic5AiJF98NTXdlRd8V_kWko=w16383'
st.sidebar.image(icon_path, width=170)

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
    #st.markdown("[![Linkedin](www.linkedin.com/in/sebascarmona)](linkedin.png)")
    st.image('https://drive.google.com/uc?export=view&id=1M_u1fZsSSCWwu88S4ts8ynw_bFDtB2iX', caption='', width=70)
    st.markdown(f"[Linkedin](https://www.linkedin.com/in/sebascarmona)", unsafe_allow_html=True)


with col2:
    #st.markdown("[![Linkedin](www.linkedin.com/in/sebascarmona)](linkedin.png)")
    st.image('https://drive.google.com/uc?export=view&id=14Ks568aUeZbkRlQoHdC0qL4ZUVHJl4lx', caption='', width=70)
    st.markdown(f"[Github](https://github.com/Sebasc322)", unsafe_allow_html=True)

with col3:
    #st.markdown("[![Linkedin](www.linkedin.com/in/sebascarmona)](linkedin.png)")
    st.image('https://drive.google.com/uc?export=view&id=1QKyL5SulGWYfuqcmDN1JvsNgVeSJM04-', caption='', width=70)
    st.markdown(f"[Medium](https://sebascar322.medium.com/)", unsafe_allow_html=True)

with col4:
    #st.markdown("[![Linkedin](www.linkedin.com/in/sebascarmona)](linkedin.png)")
    st.image('https://drive.google.com/uc?export=view&id=1STGtVysd1tFS1rMeTyQYvacQ2cmX1Qmn', caption='', width=70)
    st.markdown(f"[Portfolio](https://www.sebascarmona.com/)", unsafe_allow_html=True)
