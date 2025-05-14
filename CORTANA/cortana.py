import nltk
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import nltk
import random
import string  # to process standard python strings

# load data:
f = open('chatbot1.txt', 'r', errors='ignore')
m = open('chatbot2.txt', 'r', errors='ignore')
checkpoint = "./chatbot_weights.ckpt"

# setting up things first:
raw = f.read()
rawone = m.read()
raw = raw.lower()  # converts to lowercase
rawone = rawone.lower()  # converts to lowercase
nltk.download('punkt')  # first-time use only
nltk.download('wordnet')  # first-time use only
sent_tokens = nltk.sent_tokenize(raw)  # converts to list of sentences
word_tokens = nltk.word_tokenize(raw)  # converts to list of words
sent_tokensone = nltk.sent_tokenize(rawone)  # converts to list of sentences
word_tokensone = nltk.word_tokenize(rawone)  # converts to list of words

sent_tokens[:2]
sent_tokensone[:2]

word_tokens[:5]
word_tokensone[:5]

lemmer = nltk.stem.WordNetLemmatizer()

# function:
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

# function:
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

Introduce_answer = ["Hi, my name is cortana"]
USER_GREET = ["hi", "hey", "hello", "hello there"]
BOT_GREET = ["hello there. how are doing today", "hi. how are you doing today"]
who_are_u = ["tell me about you", "who are you", "what are you"]
who_am_i = ["Hi. i am cortana. I am an intelligent chatbot. I am designed for text based input analysing and responding purposes. I am designed by Mr.Vishwa"]
what_you_can = ["What you can do", "what can you do"]
what_you_can_a = ["I was designed as a chatbot for text inputs. I can basically talk as a chat bot and give answers to your questions."]
interlink_q = ["tell me about interlink ai", "what is interlink ai"]
interlink_a = ["interlink ai is a tech start up company that is focusing on building intelligent virtual assistants for future."]
