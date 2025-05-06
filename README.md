"# pythonlibs" 
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from collections import Counter
import spacy
from textblob import TextBlob
from langdetect import detect

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "John is running very fast in the marathon! He lives in New York. Amazing effort by him."

print("Original Text:\n", text)

# 1. Sentence Tokenization
sentences = sent_tokenize(text)
print("\n1. Sentence Tokenization:", sentences)

# 2. Word Tokenization
tokens = word_tokenize(text)
print("\n2. Word Tokenization:", tokens)

# 3. Stopword Removal
stop_words = set(stopwords.words('english'))
filtered = [w for w in tokens if w.lower() not in stop_words and w not in string.punctuation]
print("\n3. Stopword Removal:", filtered)

# 4. Stemming
stemmer = PorterStemmer()
stemmed = [stemmer.stem(word) for word in filtered]
print("\n4. Stemming:", stemmed)

# 5. Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(word) for word in filtered]
print("\n5. Lemmatization:", lemmatized)

# 6. Part-of-Speech (POS) Tagging
pos_tags = nltk.pos_tag(tokens)
print("\n6. POS Tagging:", pos_tags)

# 7. Word Frequency Counting
word_freq = Counter(filtered)
print("\n7. Word Frequency:", word_freq)

# 8. Named Entity Recognition (NER) using spaCy
doc = nlp(text)
print("\n8. Named Entities:")
for ent in doc.ents:
    print(ent.text, "-", ent.label_)

# 9. Bag-of-Words (BOW)
bow = Counter(filtered)
print("\n9. Bag of Words:", dict(bow))

# 10. Sentiment Analysis
blob = TextBlob(text)
print("\n10. Sentiment Analysis:")
print("Polarity:", blob.sentiment.polarity)
print("Subjectivity:", blob.sentiment.subjectivity)

# 11. Language Detection
lang = detect(text)
print("\n11. Language Detection:", lang)

# 12. Translation (English to French)
translated = blob.translate(to='fr')
print("\n12. Translated to French:", translated)

# 13. Spelling Correction
incorrect = "Hee is runingg veryy fasstt"
corrected = str(TextBlob(incorrect).correct())
print("\n13. Spelling Correction:")
print("Original:", incorrect)
print("Corrected:", corrected)
