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
from io import BytesIO
import xlsxwriter
from PIL import Image

# Set Path
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir /"styles"/"main.css"
sample_img = current_dir/"styles"/"sample.PNG"

# set_page_config adalah metode yang digunakan untuk mengubah setup halaman
st.set_page_config(
    page_title="Sentiment Analysis App",
    layout="wide"
)

with open(css_file) as f:
    st.markdown("<style>{}</style".format(f.read()), unsafe_allow_html=True)

# ==========================================================================================================
# Init Variable
# ==========================================================================================================
translator = Translator()
stopword_id = stopwords.words('indonesian')
image = Image.open(sample_img)

# ==========================================================================================================
# template CSV Sentiment Analysis
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
    
    
st.header('Excel Sentiment Analysis')
with st.expander('Pastikan kolom yang akan dianalisa diberikan nama judul kolom dengan review'):
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image(
            image, 
            caption='sample upload Excel',
            width=500,
        )
        
    upl = st.file_uploader('Upload Excel File')

    if upl:
        df = pd.read_excel(upl)
        # del df['Unnamed: 0']
        df['review_clean'] = df['review'].apply(textProcessing2)
        df['translated'] = df['review_clean'].apply(translate)
        df['score'] = df['translated'].apply(score)
        df['sentiment'] = df['score'].apply(analyze)
        st.write(df.head())
        
        df1 = df[["review","review_clean","translated","score",'sentiment']].copy()
        
        @st.cache_data
        def to_excel(df):
            output = BytesIO()
            writer = pd.ExcelWriter(output, engine='xlsxwriter')
            df.to_excel(writer, index=False, sheet_name='Sentiment Analysis')
            workbook = writer.book
            worksheet = writer.sheets['Sentiment Analysis']
            # format1 = workbook.add_format({'num_format': '0.00'}) 
            # worksheet.set_column('A:A', None, format1)  
            writer.close()
            processed_data = output.getvalue()
            return processed_data

        df_xlsx = to_excel(df1)  
        
        # temp = excel.read()

        st.download_button(
            label="📥 Download data dalam Excel",
            data=df_xlsx,
            file_name='sentiment.xlsx',
            # mime='text/xlsx',
        )
        

