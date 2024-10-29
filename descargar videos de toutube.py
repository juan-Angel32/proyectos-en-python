from pytube import YouTube
import os

def descargar_video(url):
    try:
        # Crea un objeto YouTube
        video = YouTube(url)

        # Muestra los detalles del video
        print(f'Título: {video.title}')
        print(f'Duración: {video.length} segundos')
        print(f'Dimensión del video: {video.file_size / (1024 * 1024):.2f} GB')

        # Obtiene el directorio del escritorio
        desktop_path = os.path.join(os.path.join(os.environ['Windows']), 'Desktop')

        # Descarga el video con la mayor resolución disponible en el escritorio
        video_stream = video.streams.get_highest_resolution()
        video_stream.download(desktop_path)

        print('Descarga finalizada. El videoclip ha sido guardado en el escritorio.')
    except Exception as e:
        print(f'Ocurrió un error: {str(e)}')

if __name__ == "__main__":
    # Introduce la URL del video de YouTube
    url = input("Introduce la URL del video de YouTube: ")
    descargar_video(url)
