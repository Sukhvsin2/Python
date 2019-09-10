import pandas as pd
import cv2
import numpy as np

wb = pd.read_csv('attendance2019-07-21.csv')

date, event, name, club = wb["Date"],wb["Event"],wb["Name"],wb["Club"]
date = list(date)
event = list(date)
name = np.asarray(name)
club = list(club)


for i in range(3):
    n = name[i]
    print(n)
    fontscale = 0.8
    fontface = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    img = cv2.imread('certificate.jpg')
    if len(n) > 10:
        x, y = 480, 400
    else:
        x, y = 340, 400
    cv2.putText(img, n , (x,y), fontface, fontscale, (0,0,0))
    cv2.imwrite("output" + str(i) +".jpg", img)
