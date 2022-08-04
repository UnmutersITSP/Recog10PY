import requests
import csv
import time
from gtts import gTTS
import os

def record(name):
    f = open('records.csv', 'a')
    csv_file = csv.writer(f)
    data = [0]*13
    i=0
    while i<100:
        try:
            r = requests.get("http://192.168.4.1/JSON")
        except:
            continue
        values = r.json()["hall"] + r.json()["mpu"]
        data = [data[x]+values[x] for x in range(13)]
        print(str(i+1)+"/100")
        i+=1
        time.sleep(0.1)
    data = [x/100 for x in data]
    csv_file.writerow([name]+data)
    f.close()
    time.sleep(1)
    print("generating mp3 file....")
    tts = gTTS(text = name , lang = 'en' , slow = False , tld = 'co.in')
    tts.save("audio/"+name+".mp3")
    print("mp3 file generated")
    print("sign recorded")

record("thumbsup")
