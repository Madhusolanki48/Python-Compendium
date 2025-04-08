# JSON PACKAGE
import json

# NUMPY PACKAGE
import numpy as np

a = np.zeros(10)  # creates an array with n number of zeroes inside it.
print(a)

b = np.full((2,10), 0.7)  #creates a two-dimensional matrix of dimensions 2 x 10 consisting only of the values 0.7.
print(b)

c = np.linspace(0,25,7)   #generates 7 equally spaced values between 0 and 25, including both endpoints
print(c)

print(type(c))

# PANDAS PACKAGE
import pandas as pd
a = pd.DataFrame({'Animals': ['Dog','Cat','Lion','Cow','Elephant'],
                    'Sounds':['Barks','Meow','Roars','Moo','Trumpet']})
print(a)
print(a.describe())  #will give the count, frequency, top values and frequency among other values.

b = pd.DataFrame({
    "Letters" : ['a', 'b', 'c', 'd', 'e', 'f'],
    "Numbers" : [12, 7, 9, 3, 5, 1]  })
print(b.sort_values(by="Numbers"))

b = b.assign(new_values = b['Numbers']*3)
print(b)


# NLTK PACKAGE
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."

# Print statement 1
print(word_tokenize(text))
# This takes the text and produces the first part of the output in which the words are tokenized, meaning they are separated into individual components, including punctuation and contractions (e.g., splitting "industry's" into ["industry", "'s"])
# Print statement 2
print(nltk.tokenize.sent_tokenize(text))  #sent_tokenize() tokenizes the block of text into sentences, producing the second part of the output

stopwords = stopwords.words("english")
new_text = []
for i in text.split():
    if i not in stopwords:
        new_text.append(i)

# Print statement 3
print(new_text)

