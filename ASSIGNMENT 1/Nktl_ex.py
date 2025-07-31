import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk import pos_tag

# Download required resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')

# Function to map POS tag to WordNet POS
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

# Example string
example_string = "My name is Harshada. I am from Shrirampur. Currently I am staying at Kopargaon. I am a B.Tech student at SCOE."
# Sentence Tokenization
sentences = sent_tokenize(example_string)
print("Sentence Tokenization:")
print(sentences)

# Word Tokenization
words = word_tokenize(example_string)
print("\nWord Tokenization:")
print(words)

# Remove Stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]
print("\nFiltered Words (without stopwords):")
print(filtered_words)

# Stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]
print("\nStemmed Words (after removing stopwords):")
print(stemmed_words)

# POS Tagging for Lemmatization
pos_tags = pos_tag(filtered_words)

# Lemmatization with POS
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word, get_wordnet_pos(pos)) for word, pos in pos_tags]
print("\nLemmatized Words (after removing stopwords):")
print(lemmatized_words)





" outptut of the code "

"""
Sentence Tokenization:
['The researchers were analyzing large datasets to discover hidden patterns and insights that could improve decision-making in healthcare.', 'Their findings suggested that machine learning models outperform traditional statistical methods in many cases.']

Word Tokenization:
['The', 'researchers', 'were', 'analyzing', 'large', 'datasets', 'to', 'discover', 'hidden', 'patterns', 'and', 'insights', 'that', 'could', 'improve', 'decision-making', 'in', 'healthcare', '.', 'Their', 'findings', 'suggested', 'that', 'machine', 'learning', 'models', 'outperform', 'traditional', 'statistical', 'methods', 'in', 'many', 'cases', '.']

Filtered Words (without stopwords):
['researchers', 'analyzing', 'large', 'datasets', 'discover', 'hidden', 'patterns', 'insights', 'could', 'improve', 'decision-making', 'healthcare', '.', 'findings', 'suggested', 'machine', 'learning', 'models', 'outperform', 'traditional', 'statistical', 'methods', 'many', 'cases', '.']

Stemmed Words (after removing stopwords):
['research', 'analyz', 'larg', 'dataset', 'discov', 'hidden', 'pattern', 'insight', 'could', 'improv', 'decision-mak', 'healthcar', '.', 'find', 'suggest', 'machin', 'learn', 'model', 'outperform', 'tradit', 'statist', 'method', 'mani', 'case', '.']

Lemmatized Words (after removing stopwords):
['researcher', 'analyze', 'large', 'datasets', 'discover', 'hide', 'pattern', 'insight', 'could', 'improve', 'decision-making', 'healthcare', '.', 'finding', 'suggest', 'machine', 'learning', 'model', 'outperform', 'traditional', 'statistical', 'method', 'many', 'case', '.']
"""