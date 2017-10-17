# Wattary's Ear
# NOTE: this file requires NLTK & PyAudio & Python Speech Recognition Engine because it uses the Microphone class

#Importing the modules
import speech_recognition as sr
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

#-------------------------- Speech Recognition : Speech-to-text -----------------------------------#

# obtaining audio from the microphone
Ear = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening!")
    audio = Ear.listen(source)

# recognize speech using Google Speech Recognition
# for testing purposes, we're just using the default API key
# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")` instead of `r.recognize_google(audio)`

try:
    # Saving recognized text into text variable
    text = Ear.recognize_google(audio)
except sr.UnknownValueError:
    print("I can't hear you, Could you repeat that please? ")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

#----------------------------------------- NLP Pipeline ------------------------------------------#

#----------------------------------- Sentence Splitting ------------------------------------------#

# Performing sentence tokenization and saving the result into sentences list in order to parse each one seperately.
sentences = sent_tokenize(text)

#----------------------------------------- Word Tokenization ------------------------------------------#

# Performing word tokenization over the resulted sentences and save the result into a new list of lists called tokens.
tokens = [word_tokenize(sentence) for sentence in sentences]
