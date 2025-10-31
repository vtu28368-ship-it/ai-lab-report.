import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

text = "The striped bats are hanging"

lemmatizer = WordNetLemmatizer()
words = word_tokenize(text)

print("Original words → Lemmatized words\n")
for word in words:
    print(f"{word} → {lemmatizer.lemmatize(word)}")
