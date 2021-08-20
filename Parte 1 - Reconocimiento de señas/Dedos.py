import cv2
import mediapipe as mp
import os

nombre = 'no me gusta'
direccion = 'C:/Users/joseg/Documents/copias/Data'
carpeta = direccion + '/' + nombre

if not os.path.exists(carpeta):
    print('carpeta creada: ', carpeta)
    os.makedirs(carpeta)


#contador fotos

cont = 0


#leer camara
camera_port = 0
cap = cv2.VideoCapture(0)


#objeto para almacenar la detección y el siguimiento de las manos

clase_manos = mp.solutions.hands

manos = clase_manos.Hands()



#metodo dibujar manos

dibujo = mp.solutions.drawing_utils

while(1):
    ret, frame = cap.read()
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    copia = frame.copy()
    resultado = manos.process(color)
    posiciones = []

    if resultado.multi_hand_landmarks:
        for mano in resultado.multi_hand_landmarks:
            for id, lm in enumerate(mano.landmark):

                alto, ancho, c = frame.shape
                corx, cory = int(lm.x*ancho), int(lm.y*alto)
                posiciones.append([id,corx,cory])
                dibujo.draw_landmarks(frame,mano,clase_manos.HAND_CONNECTIONS)

            if len(posiciones) != 0:
                pto_i1 = posiciones[4]
                pto_i2 = posiciones[20]
                pto_i3 = posiciones[12]
                pto_i4 = posiciones[0]
                pto_i5 = posiciones[9]
                x1,y1 = (pto_i5[1]-150),(pto_i5[2]-140)
                ancho, alto = (x1+200),(y1+200)
                x2, y2 = x1 + ancho, y1 + alto
                dedos_reg = copia[y1:y2, x1:x2]
                cv2.rectangle(frame,(x1, y1), (x2,y2),(0,255,0), 3)
            dedos_reg =  cv2.resize(dedos_reg,(200,200), interpolation = cv2.INTER_CUBIC)
            cv2.imwrite(carpeta + "/dedos_{}.png".format(cont), dedos_reg)
            cont = cont + 1


    cv2.imshow("Video",frame)
    k = cv2.waitKey(1)
    if k == 27 or cont >= 300:
        break

cap.release()
cv2.destroyAllWindows()