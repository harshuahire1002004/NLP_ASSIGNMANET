###  Assignment No 5 ###

"""Assignment Title :  Implement regular expression function to find URL, IP address, Date,
PAN number in textual data using python libraries"""


import spacy
import re

# Load the spaCy English language model
nlp = spacy.load("en_core_web_sm")

# Define regular expressions
url_pattern = re.compile(r'https?://\S+|www\.\S+')

ip_address_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
pan_number_pattern = re.compile(r'[A-Z]{5}[0-9]{4}[A-Z]')

def extract_entities(text):
    # Tokenize the text using spaCy
    doc = nlp(text)

    # Find entities using regular expressions
    urls = re.findall(url_pattern, text)
    ip_addresses = re.findall(ip_address_pattern, text)
    dates = re.findall(date_pattern, text)
    pan_numbers = re.findall(pan_number_pattern, text)

    # Extract spaCy entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    return {
        'urls': urls,
        'ip_addresses': ip_addresses,
        'dates': dates,
        'pan_numbers': pan_numbers,
        'spaCy_entities': entities
    }


# Example usage
text_data = """
Check out this example with a reference site: https://dataSecure.in
.
The system IP address is 192.0.2.145.
The document date is 2022-11-30.
The PAN code provided is LMNOP2345K.
"""

results = extract_entities(text_data)

print("URLs:", results['urls'])
print("IP Addresses:", results['ip_addresses'])
print("Dates:", results['dates'])
print("PAN Numbers:", results['pan_numbers'])
print("Entities:", results['spaCy_entities'])


'''
**************   OUTPUT     ****************
URLs: ['https://dataSecure.in']
IP Addresses: ['192.0.2.145']
Dates: ['2022-11-30']
PAN Numbers: ['LMNOP2345K']
Entities: [('IP', 'ORG'), ('192.0.2.145', 'DATE'), ('2022-11-30', 'DATE'), ('PAN', 'ORG'), ('LMNOP2345K.', 'GPE')]

'''
