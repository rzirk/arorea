import numpy as np
import cv2
import ImageProcessing as ip
import util
from gtts import gTTS
from io import BytesIO
from playsound import playsound
import requests
import time

def tellColor():
    #%%
    #capture from camera at location 0
    #cap = cv2.VideoCapture(0)
    #ret, img = cap.read()
    img_name = 'test.jpg'
    img = cv2.imread(img_name)

    #Region of intrest
    height, width, channels = img.shape
    size_in_px = 100

    print(width/2-size_in_px,
    height/2+size_in_px,
    width/2+size_in_px,
    height/2-size_in_px)

    #x and y are flipped... fuck this shit img[y:y+h, x:x+w]
    gaze = img[int(height/2-size_in_px):int(height/2 + size_in_px),
    int(width/2-size_in_px):int(width/2 + size_in_px)].copy()

    cv2.rectangle(img,
    (int(width/2-size_in_px), int(height/2+size_in_px)),
    (int(width/2+size_in_px), int(height/2-size_in_px)),(0,255,0),3)


    #gaze = img(region_of_interest)
    cv2.imshow('img',img)
    cv2.imshow('gaze',gaze)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #Select region of intrest
    #roi = cv2.selectROI(img)
    #gaze =  img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

    lables, centers = ip.get_dominant_colors(gaze)
    #%%
    colors = ip.pixelCount(lables,centers)
    print(colors)

    #%%
    #Colors to Names
    for index, color in enumerate(colors):   
        actual_name, closest_name = util.get_colour_name(color[0])
        print ("Actual colour name:", actual_name, ", closest colour name:", closest_name, "Anmount: ",color[1], "RGB: ",color[0])
        color[0] = closest_name
        colors[index] = color

    colors = list(util.accumulate(colors))
    print(colors)
    colors.sort(key=lambda x: x[1],reverse=True)
    print(colors)

    #Translate  colors
    color1 = colors[0][0]
    color2 = colors[1][0]

    color1 = util.translate_css_21_color(color1)
    color2 = util.translate_css_21_color(color2)
    text = color1 + " und " + color2 + "."

    #Speak
    tts = gTTS(text, lang='de')
    tts.save('test.mp3')
    playsound('test.mp3')

    #cv2.VideoCapture(0).release()

def tell_what_you_see():

    print("Start")
    time.sleep(1)
    print("Done sleeping")
    
    #capture from camera at location 0
    #cap = cv2.VideoCapture(0)
    img_name = 'test.jpg'
    img = cv2.imread(img_name)

    url = 'http://localhost:5000/model/predict'
    #files = {'file' : img}
    headers = {'accept' : 'application/json', }
    files = {'image': (img_name, open(img_name, 'rb'), 'image/jpeg')}
    r = requests.post(url=url, files=files, headers=headers)
    data = r.json()

    text = data['predictions'][0]['caption']

    url_uebersetzung = 'https://translation.googleapis.com/language/translate/v2'
    key = '<Your API Key Here>'
    parameter = {'q' : text, 'target' : 'de', 'format' : 'text', 'source': 'en', 'key' : key }
    r = requests.post(url = url_uebersetzung, data=parameter)
    print (text)

    data = r.json()

    print(data)

    text = data['data']['translations'][0]['translatedText']
    print (text)

    #Speak
    tts = gTTS(text, lang='de')
    tts.save('test2.mp3')
    playsound('test2.mp3')

    print("Done")

    #cv2.VideoCapture(0).release()

