#coding: utf-8
#_-_Autor: Erlon_-_

import cv2

padraoRostos = cv2.CascadeClassifier('C:\\Users\\FABIANA\\IdeaProjects\\terceira-nota-pdi\\classificadores\\cat_face.xml')

def gatinhos(gatos) :
	imagem = cv2.imread(gatos)
	imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
	faceDetect = padraoRostos.detectMultiScale(imagemCinza, scaleFactor=1.1, minNeighbors=7, minSize=(75,80))

	numero_de_gatinhos = 0

	for (x, y, l, a) in faceDetect:
		# Mostrar as coordenadas x, y, largura e altura de cada ocorrência
		print(f'Coordenadas da ocorrência {numero_de_gatinhos + 1}:')
		print(f'X: {x}')
		print(f'Y: {y}')
		print(f'Largura: {l}')
		print(f'Altura: {a}')

		cv2.rectangle(imagem, (x, y), (x + l, y + a), (255, 0, 0), 5)

		numero_de_gatinhos += 1

	print(f'Total de gatos identificados: {numero_de_gatinhos}')

	for (x, y, l, a) in faceDetect:
		cv2.rectangle(imagem, (x, y), (x + l, y + a), (255, 0, 0), 5)

	cv2.imshow("Faces encontradas", imagem)
	cv2.waitKey()

#IMAGENS COM GATOS
gatinhos('C:\\Users\\FABIANA\\IdeaProjects\\terceira-nota-pdi\\images\\gatos1.webp')
gatinhos('C:\\Users\\FABIANA\\IdeaProjects\\terceira-nota-pdi\\images\\gatos2.webp')
gatinhos('C:\\Users\\FABIANA\\IdeaProjects\\terceira-nota-pdi\\images\\gatos3.jpg')
gatinhos('C:\\Users\\FABIANA\\IdeaProjects\\terceira-nota-pdi\\images\\gatos4.jpg')
gatinhos('C:\\Users\\FABIANA\\IdeaProjects\\terceira-nota-pdi\\images\\gatos5.webp')
gatinhos('C:\\Users\\FABIANA\\IdeaProjects\\terceira-nota-pdi\\images\\gatos6.jpg')
gatinhos('C:\\Users\\FABIANA\\IdeaProjects\\terceira-nota-pdi\\images\\gatos7.webp')
gatinhos('C:\\Users\\FABIANA\\IdeaProjects\\terceira-nota-pdi\\images\\gatos8.jpeg')
gatinhos('C:\\Users\\FABIANA\\IdeaProjects\\terceira-nota-pdi\\images\\gatos9.jpg')
gatinhos('C:\\Users\\FABIANA\\IdeaProjects\\terceira-nota-pdi\\images\\gatos10.png')
gatinhos('C:\\Users\\FABIANA\\IdeaProjects\\terceira-nota-pdi\\images\\gatos11.jpg')
gatinhos('C:\\Users\\FABIANA\\IdeaProjects\\terceira-nota-pdi\\images\\gatos12.jpg')
gatinhos('C:\\Users\\FABIANA\\IdeaProjects\\terceira-nota-pdi\\images\\gatos13.jpeg')
gatinhos('C:\\Users\\FABIANA\\IdeaProjects\\terceira-nota-pdi\\images\\gatos14.webp')
gatinhos('C:\\Users\\FABIANA\\IdeaProjects\\terceira-nota-pdi\\images\\gatos15.webp')
#IMAGENS SEM GATOS
gatinhos('C:\\Users\\FABIANA\\IdeaProjects\\terceira-nota-pdi\\images\\naogatos1.jpg')
gatinhos('C:\\Users\\FABIANA\\IdeaProjects\\terceira-nota-pdi\\images\\naogatos2.webp')
gatinhos('C:\\Users\\FABIANA\\IdeaProjects\\terceira-nota-pdi\\images\\naogatos3.jpg')
gatinhos('C:\\Users\\FABIANA\\IdeaProjects\\terceira-nota-pdi\\images\\naogatos4.jpg')
gatinhos('C:\\Users\\FABIANA\\IdeaProjects\\terceira-nota-pdi\\images\\naogatos5.png')




