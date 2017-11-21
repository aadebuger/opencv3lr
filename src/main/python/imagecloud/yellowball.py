#encoding=utf-8
'''
Created on 2017年11月14日

@author: aadebuger
'''

import cv2
 
# initialisiere Webcam
cam = cv2.VideoCapture(1)
 
# definiere Farb-Ranges
lower_yellow = (18, 100, 210)
upper_yellow = (40, 160, 245)
 
# zeige Stream von WebCam an
while cam.isOpened():
    # lese frame von WebCam
    ret, frame = cam.read()
 
    # konvertiere Frame in HSV-Farbraum, um besser nach Farb-Ranges filtern zu können
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 
    # filtere Bild nach Farbgrenzen
    mask = cv2.inRange(frame, lower_yellow, upper_yellow)
 
    # finde Konturen in der Maske, die nur noch zeigt, wo gelbe Pixel sind:
    _, contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                      cv2.CHAIN_APPROX_SIMPLE)
 
    # suche die größte Kontur heraus (diese ist höchst wahrscheinlich der Tennisball)
    # dazu nehmen wir die Fläche der Kontur:
    if len(contours) > 0:
        tennis_ball = max(contours, key=cv2.contourArea)
 
        # zeichne die Bounding box des Tennisballs in das Video-Bild ein:
        x, y, w, h = cv2.boundingRect(tennis_ball)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=3)
 
    # zeige Frame an
    cv2.imshow("frame", frame)
 
    # warte auf Tastendruck (sonst sieht man das Fenster nicht)
    key = cv2.waitKey(1) & 0xff
 
    # wenn ESC gedrückt, beende Programm
    if key == 27:
        break


if __name__ == '__main__':
    pass
