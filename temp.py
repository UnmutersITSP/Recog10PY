import os
from gtts import gTTS
import csv

with open("records.csv","r") as f:
    reader = csv.reader(f)
    data = list(reader)
    data_dict = {}
    for sign in data:
        # skip any empty lines
        if len(sign) == 0:
            continue

        data_dict[sign[0]] = sign[1:]

    for x in list(data_dict.keys()):
        tts = gTTS(text = x,lang="en",slow = False,tld = "co.in")
        tts.save("audio/"+x+".mp3")
        print("mp3 file generated")