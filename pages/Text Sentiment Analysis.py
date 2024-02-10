import streamlit as st
import pandas as pd
from pathlib import Path
from textblob import TextBlob
from googletrans import Translator
import re, string,json
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from typing import List
from nlp_id.lemmatizer import Lemmatizer
from nlp_id.tokenizer import Tokenizer, PhraseTokenizer
from nlp_id.postag import PosTag
from nlp_id.stopword import StopWord
import nltk

# Set Path
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir /"styles"/"main.css"


# set_page_config adalah metode yang digunakan untuk mengubah setup halaman
st.set_page_config(
    page_title="Text Sentiment Analysis - Stephen Hendry",
    layout="wide"
)

with open(css_file) as f:
    st.markdown("<style>{}</style".format(f.read()), unsafe_allow_html=True)

# init var
translator = Translator()
stopword_id = stopwords.words('indonesian')


# function
def cekSentimentText(nilai):
    if nilai < 0:
        st.write('Hasil sentiment adalah negatif')
    elif nilai == 0:
        st.write('hasil sentiment adalah netral')
    else:
        st.write('hasil sentiment adalah Positif')
        
def textProcessing(inputan):
    lower = inputan.lower()
    
    #number
    numberClean = re.sub(r"\d+", "", lower)
    
    #@pattern
    at_pattern = re.compile(r'@\S+')
    patternClean = at_pattern.sub(r'', numberClean)
    
    #punctuation
    punctuationClean = patternClean.translate(str.maketrans("","",string.punctuation))
    
    #whitespace  
    ws = punctuationClean.strip()
    
    #url
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    urlClean = url_pattern.sub(r'', ws)

    # Tokenization
    result = word_tokenize(urlClean)
    
    # Stopword
    resultwords = [word for word in result if word not in stopword_id]
    result = ' '.join(resultwords)
    
    st.write('Hasil Text Cleaning adalah : ', result)


# ==========================================================================================================
# template Sentiment Analysis
# ==========================================================================================================
st.header('Sentiment Analysis')
with st.expander("Analisa Sentiment Text"):
    input1 = st.text_input('Input Text Disini: ')
    if input1:
        hasil = str(translator.translate(input1).text)
        blob = TextBlob(hasil)
        polaritas = round(blob.sentiment.polarity,2)
        subjektivitas = round(blob.sentiment.subjectivity,2)
        st.write('Polaritas : ', polaritas)
        st.write('Subjektivitas : ', subjektivitas)
        st.write('Hasil translate :', hasil)
        cekSentimentText(polaritas)
st.write("---")

# ==========================================================================================================
# template Text Cleaning
# ==========================================================================================================
st.header('Text Cleaning')
pre = st.text_input('Input Text untuk Text Cleaning : ')
if pre:
    textProcessing(pre)
st.write("---")

# ==========================================================================================================
# template CSV Sentiment Analysis
# ==========================================================================================================

# def translate(x):
#     hasil = str(translator.translate(x).text)
#     return hasil

# def score(x):
#     blob1 = TextBlob(x)
#     return blob1.sentiment.polarity

# def analyze(x):
#     if x < 0:
#         return 'Negatif'
#     elif x == 0:
#         return 'Netral'
#     else:
#         return 'Positif'

# def textProcessing2(x):
#     lower = x.lower()
    
#     #number
#     numberClean = re.sub(r"\d+", "", lower)
    
#     #@pattern
#     at_pattern = re.compile(r'@\S+')
#     patternClean = at_pattern.sub(r'', numberClean)
    
#     #punctuation
#     punctuationClean = patternClean.translate(str.maketrans("","",string.punctuation))
    
#     #whitespace  
#     ws = punctuationClean.strip()
    
#     #url
#     url_pattern = re.compile(r'https?://\S+|www\.\S+')
#     urlClean = url_pattern.sub(r'', ws)

#     # Tokenization
#     result = word_tokenize(urlClean)
    
#     # Stopword
#     resultwords = [word for word in result if word not in stopword_id]
#     result = ' '.join(resultwords)
    
#     return result
    
    
# st.header('CSV Sentiment Analysis')
# with st.expander('Pastikan kolom yang akan dianalisa diberikan nama judul kolom dengan review'):
#     upl = st.file_uploader('Upload CSV')

#     if upl:
#         df = pd.read_csv(upl)
#         # del df['Unnamed: 0']
#         df['review_clean'] = df['review'].apply(textProcessing2)
#         df['translated'] = df['review_clean'].apply(translate)
#         df['score'] = df['translated'].apply(score)
#         df['analysis'] = df['score'].apply(analyze)
#         st.write(df.head())
        
#         @st.cache_data
#         def convert_df(df):
#             return df.to_csv().encode('utf-8')

#         csv = convert_df(df)

#         st.download_button(
#             label="Download data dalam CSV",
#             data=csv,
#             file_name='sentiment.csv',
#             mime='text/csv',
#         )
        

