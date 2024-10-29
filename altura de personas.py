import cv2
import numpy as np

def detectar_persona(imagen):
    # Cargar el modelo de detección de personas (Upper Body)
    upper_body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_upperbody.xml')

    # Convertir la imagen a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Detectar personas en la imagen
    personas = upper_body_cascade.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(personas) > 0:
        # Devolver las coordenadas del rectángulo que rodea a la persona
        return personas[0]
    else:
        return None

def calcular_altura(rectangulo):
    # Calcular la altura en píxeles del rectángulo
    altura_pixels = rectangulo[3]

    # Supongamos una altura media de una persona adulta en centímetros
    altura_promedio_cm = 170

    # Calcular la altura en centímetros
    altura_cm = (altura_pixels / rectangulo[3]) * altura_promedio_cm

    return altura_cm

# Cargar la imagen
imagen = cv2.imread('rt.jpg')

# Detectar a la persona en la imagen
rectangulo_persona = detectar_persona(imagen)

if rectangulo_persona is not None:
    # Calcular la altura de la persona
    altura_persona = calcular_altura(rectangulo_persona)
    
    # Dibujar el rectángulo alrededor de la persona
    x, y, w, h = rectangulo_persona
    cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mostrar la altura de la persona
    cv2.putText(imagen, f'Altura: {altura_persona:.2f} cm', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Mostrar la imagen con la detección
    cv2.imshow('Detección de Altura', imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('No se detectó a ninguna persona en la imagen.')
