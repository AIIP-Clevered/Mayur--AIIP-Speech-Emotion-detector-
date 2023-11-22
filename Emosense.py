import tkinter.messagebox
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from tkinter import *
import speech_recognition as sr

nltk.download('vader_lexicon')

def getaudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        audio = r.listen(source)
        myText = r.recognize_google(audio)
    return myText

def analyze_sentiment(mainT):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(mainT)
    sentiment = ""
    if sentiment_scores['compound'] >= 0.05:
        sentiment = "positive"
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    return sentiment

def display_response():
    mainT = getaudio()
    emotion = analyze_sentiment(mainT)
    response_text.set("Response: " + emotion)

   # Tkinter GUI
root = Tk()
root.title("Speech Emotion Recognition")

canvas1 = Canvas(root, width=340, height=400, bg="black")
canvas1.pack()

img = PhotoImage(file="C:/Users/mayur/Downloads/mike-removebg-preview.png")
canvas1.create_image(1, 1, anchor=NW, image=img)

button_record = Button(root, text='Record Voice', command=display_response, bg='orange', font=("Helvetica", 16, "bold"), fg='white')
canvas1.create_window(175, 100, window=button_record)

button_stop = Button(root, text='Stop Recording', command=root.quit, bg='red', font=("Helvetica", 12, "bold"), fg='white')
canvas1.create_window(175, 150, window=button_stop)

label_title = Label(root, text='SPEECH EMOTION RECOGNITION', font=("Helvetica", 16, "bold"), bg='black', fg='white')
canvas1.create_window(173, 50, window=label_title)

response_text = StringVar()
response_box = Entry(root, textvariable=response_text, font=("Helvetica", 14), state='readonly', width=30, justify='center', bg="white")
canvas1.create_window(173, 200, window=response_box)

root.mainloop()
