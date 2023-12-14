#coding: utf-8
#_-_Autor: Erlon_-_

import cv2

# Carregar o classificador Haar Cascade para detecção de rostos
padraoRostos = cv2.CascadeClassifier('C:\\Users\\FABIANA\\IdeaProjects\\terceira-nota-pdi\\classificadores\\cat_face.xml')

# Iniciar captura de vídeo da webcam
cap = cv2.VideoCapture(0)

while True:
    # Capturar frame a frame da webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Converter para escala de cinza
    imagemCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostos
    faceDetect = padraoRostos.detectMultiScale(imagemCinza, scaleFactor=1.2, minNeighbors=3, minSize=(90,100))
    
    # Desenhar retângulos ao redor dos rostos detectados
    for (x, y, l, a) in faceDetect:
        cv2.rectangle(frame, (x, y), (x+l, y+a), (255, 0, 0), 5)

    # Exibir o frame com as detecções
    cv2.imshow("Faces encontradas", frame)

    # Sair com a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a captura e fechar todas as janelas
cap.release()
cv2.destroyAllWindows()
