import spacy
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Sample climate policy text
climate_text = """The Paris Agreement commits nations to reducing carbon emissions significantly by 2030. 
It emphasizes international cooperation, renewable energy transition, and enforcing carbon taxes."""

# Process text with spaCy
doc = nlp(climate_text)

# Extract named entities (organizations, agreements, countries)
print("Entities in text:", [(ent.text, ent.label_) for ent in doc.ents])

# Tokenize and filter key terms
tokens = word_tokenize(climate_text.lower())
filtered_tokens = [word for word in tokens if word not in stopwords.words("english")]

# Most common words (policy insights)
print("Most frequent terms:", Counter(filtered_tokens).most_common(5))
