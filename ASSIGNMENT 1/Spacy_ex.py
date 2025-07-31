import spacy
from spacy.lang.en.stop_words import STOP_WORDS

# Load the English model
nlp = spacy.load("en_core_web_sm")

# Input text
about_text = ( "My name is Harshada Ahire, currently studying as a third-year B.Tech IT student at Sanjivani College of Engineering, Kopargaon (Roll No. 4, PRN: UIT22F1004). I have been developing multiple web applications and was working on backend systems using Node.js and frontend design using React.js. I enjoy learning new technologies and improving my programming skills daily.")

# Process text
about_doc = nlp(about_text)

# Print each token and its index
for token in about_doc:
    print(token, token.idx)

# Print total number of stopwords
print("\nTotal spaCy Stopwords:", len(STOP_WORDS))

# Print first 10 stopwords only
print("\nFirst 10 Stopwords:")
for stop_word in list(STOP_WORDS)[:10]:
    print(stop_word)

print("Token\t→ Lemma")
for token in about_doc:
    print(f"{token.text}\t→ {token.lemma_}")  
