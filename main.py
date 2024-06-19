import os
import sys
import platform

try:
    from pytube import YouTube
    from pytube.innertube import _default_clients as client
except ImportError:
    # Se o Pytube não estiver instalado, instale-o automaticamente
    print("Pytube não encontrado. Instalando automaticamente...")
    if platform.system() == "Linux":
        os.system("sudo apt install pytube")
    elif platform.system() == "Darwin":
        os.system("brew install pytube")
    elif platform.system() == "Windows":
        os.system("pip install pytube==15.0.0 --user")

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


def get_download_directory():
    """
    Retorna o diretório de download padrão com base no sistema operacional.
    """
    if platform.system() == "Linux":
        return os.path.join(os.path.expanduser("~"), "Música")
    elif platform.system() == "Darwin":
        return os.path.join(os.path.expanduser("~"), "Música")
    elif platform.system() == "Windows":
        return os.path.join(os.getenv("USERPROFILE"), "Downloads")
    else:
        # Retorna o diretório atual como padrão
        return os.getcwd()


if __name__ == "__main__":
    url = input("Digite a URL do vídeo do YouTube: ")
    diretorio = get_download_directory()
    baixar_musica(url, diretorio)
