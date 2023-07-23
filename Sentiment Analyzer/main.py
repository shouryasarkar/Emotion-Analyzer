# Libraries needed for nlp project
import nltk
from textblob import TextBlob

# NLTK requires additional resources like corpora for some tasks
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

text = input("Enter your emotion: ")


# It is going to analyze the text and return the text score in a continuous scale 
def get_sentiment_score(text):
    # Going to analyze the text here and tell the polarity of the text
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    # Negation handling
    # This is going to tokenize the text into list of words
    words = nltk.word_tokenize(text)

    # Currently the negation is inactive
    negate = False

    # In teh loop the i represents the index value and words represents each letters
    for i, word in enumerate(words):
        if word in ['not', 'no', 'neither', 'nor', 'never', 'nobody', 'nowhere']:
            # This means true it has negate word in the sentence
            negate = not negate
        elif word in ['.', '!', '?']:
            # Checks if the word has these punctuations if it has then it returns false again 
            negate = False
        # This line checks if there is any active negation in the sentence
        if negate:
            sentiment_score *= -1

    return sentiment_score


# Defining the sentiment analyzer
def get_sentiment(text):
    sentiment_score = get_sentiment_score(text)

    if sentiment_score < -0.5:
        return 'very negative'
    elif sentiment_score < 0:
        return 'negative'
    elif sentiment_score == 0:
        return 'neutral'
    elif sentiment_score > 0.5:
        return 'very positive'
    else:
        return 'positive'


print(get_sentiment(text))
