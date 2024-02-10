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
nltk.download('stopwords')
nltk.download('punkt')
from PIL import Image

# Set Path
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir /"styles"/"main.css"
sample_img = current_dir/"sample.png"
# sample_img = current_dir/"styles"/"sample.PNG"

# set_page_config adalah metode yang digunakan untuk mengubah setup halaman
st.set_page_config(
    page_title="CSV Sentiment Analysis - Stephen Hendry",
    layout="wide"
)

with open(css_file) as f:
    st.markdown("<style>{}</style".format(f.read()), unsafe_allow_html=True)

# init var
translator = Translator()
stopword_id = stopwords.words('indonesian')
image = Image.open(sample_img)


# ==========================================================================================================
# Function
# ==========================================================================================================

def translate(x):
    hasil = str(translator.translate(x).text)
    return hasil

def score(x):
    blob1 = TextBlob(x)
    return blob1.sentiment.polarity

def analyze(x):
    if x < 0:
        return 'Negatif'
    elif x == 0:
        return 'Netral'
    else:
        return 'Positif'

def textProcessing2(x):
    lower = x.lower()
    
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
    
    return result
    
# ==========================================================================================================
# template CSV Sentiment Analysis
# ==========================================================================================================
st.header('CSV Sentiment Analysis')
with st.expander('Pastikan kolom yang akan dianalisa diberikan nama judul kolom dengan review'):
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image(
            image, 
            caption='sample upload CSV',
            width=500,
        )
    upl = st.file_uploader('Upload CSV')

    if upl:
        df = pd.read_csv(upl)
        # del df['Unnamed: 0']
        df['review_clean'] = df['review'].apply(textProcessing2)
        df['translated'] = df['review_clean'].apply(translate)
        df['score'] = df['translated'].apply(score)
        df['sentiment'] = df['score'].apply(analyze)
        st.write(df.head())
        
        df1 = df[["review","review_clean","translated","score",'sentiment']].copy()
        
        @st.cache_data
        def convert_df(df):
            return df.to_csv().encode('utf-8')

        csv = convert_df(df1)

        st.download_button(
            label="📥 Download data dalam CSV",
            data=csv,
            file_name='sentiment.csv',
            mime='text/csv',
        )
        

