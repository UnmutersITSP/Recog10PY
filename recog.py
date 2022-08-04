import csv
import time
import requests
import os

def load_csv_to_dict():
    with open("records.csv", "r") as f:
        reader = csv.reader(f)
        data = list(reader)
        data_dict = {}
        
        for sign in data:
            # skip any empty lines
            if len(sign) == 0:
                continue

            data_dict[sign[0]] = sign[1:]
        
    return data_dict

def predict(state):
    hall_coeff = 0.1
    hall2_coeff = 0.1
    mpu_coeff = 1
    coeff_vect = [hall_coeff]*5 + [hall2_coeff]*5 + [mpu_coeff]*3
    min_error = float("inf")
    for sign in list(signs.keys()):
        error = sum([abs(float(x)-float(y))*z for x,y,z in zip(state, signs[sign], coeff_vect)])
        if error < min_error:
            min_error = error
            best_sign = sign
    
    return (min_error,best_sign)

def run_predictions():
    while True:
        try:
            r = requests.get("http://192.168.4.1/JSON")
        except:
            continue

        values = r.json()["hall"] + r.json()["mpu"]

        error, sign = predict(values)
        if error<100:
            print(sign)
            os.system("mpg321 audio/"+sign+".mp3")
        else:
            print("nope")
        time.sleep(2)

signs = load_csv_to_dict()

run_predictions()
