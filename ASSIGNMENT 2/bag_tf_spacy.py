import spacy
import re
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


nlp = spacy.load("en_core_web_sm")

paragraph =("The government announced a new economic policy. "
             "Global markets reacted positively to the news. "
             "Experts predict economic growth in the coming year. "
             "We first tokenize the text into words and create a Dictionary that assigns each word a unique ID.")



doc = nlp(paragraph)
sentences = [sent.text for sent in doc.sents]

corpus = []


for sent in sentences:
    sent = re.sub('[^a-zA-Z]', ' ', sent)  
    sent = sent.lower() 
    corpus.append(sent)

print("Processed Corpus:", corpus)


cv = CountVectorizer()
bow_features = cv.fit_transform(corpus).toarray()
print("\nBag of Words Representation:\n", bow_features)
print("Feature Names (BoW):", cv.get_feature_names_out())


tfidf = TfidfVectorizer()
tfidf_features = tfidf.fit_transform(corpus).toarray()
print("\nTF-IDF Representation:\n", tfidf_features)
print("Feature Names (TF-IDF):", tfidf.get_feature_names_out())
