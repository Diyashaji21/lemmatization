# Import necessary libraries
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# Download required resources
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')

# Initialize the WordNet Lemmatizer
lemmatizer = WordNetLemmatizer()

# Function to get wordnet POS tag
def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {'J': wordnet.ADJ,
                'N': wordnet.NOUN,
                'V': wordnet.VERB,
                'R': wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

# Sample text
text = "The striped bats are hanging on their feet for best"

# Lemmatization process
lemmatized_words = [lemmatizer.lemmatize(word, get_wordnet_pos(word)) for word in nltk.word_tokenize(text)]

# Display lemmatized words
print("Lemmatized words:", lemmatized_words)
