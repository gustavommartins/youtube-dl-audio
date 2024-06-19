import os

try:
    from pytube import YouTube
    from pytube.innertube import _default_clients as client
except ImportError:
    # Se o Pytube não estiver instalado, instale-o automaticamente
    print("Pytube não encontrado. Instalando automaticamente...")
    os.system(" pip install pytube==15.0.0 --user")

    # Importe o Pytube novamente após a instalação
    from pytube import YouTube
    from pytube.innertube import _default_clients as client

# Set a default client to AgeRestrictedError
client["ANDROID_MUSIC"] = client["ANDROID_CREATOR"]


def baixar_musica(videoUrl, diretorio_destino="."):
    try:
        video = YouTube(videoUrl)
        stream = video.streams.filter(only_audio=True).first()
        stream.download(output_path=diretorio_destino)
        print(f"O aúdio de '{video.title}' foi baixada com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao baixar o seu aúdio: {e}")


if __name__ == "__main__":
    url = input("Digite a URL do vídeo do YouTube: ")
    diretorio = "./audio_files"
    baixar_musica(url, diretorio)
