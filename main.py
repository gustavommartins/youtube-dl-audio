import sys

try:
    from pytube import YouTube
except ImportError:
    print("Pytube não encontrado. Instale-o executando 'pip install pytube'")
    sys.exit()

def baixar_musica(url, diretorio_destino="."):
    try:
        video = YouTube(url)
        stream = video.streams.filter(only_audio=True).first()
        stream.download(output_path=diretorio_destino)
        print(f"O aúdio de '{video.title}' foi baixada com sucesso.")    
    except Exception as e:
        print(f"Ocorreu um erro ao baixar o seu aúdio: {e}")

if __name__ == "__main__":
    url = input("Digite a URL do vídeo do YouTube: ")
    diretorio = "./audio_files"
    baixar_musica(url, diretorio)