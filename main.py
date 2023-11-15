try:
    from pytube import YouTube
except ImportError:
    print("Pytube não encontrado. Instale-o executando 'pip install pytube'")
    exit()

def baixar_musica(url, diretorio_destino="."):
    try:
        # Cria um objeto YouTube com a URL fornecida
        video = YouTube(url)

        # Seleciona a melhor stream de áudio disponível (formato mp4)
        stream = video.streams.filter(only_audio=True).first()

        # Baixa o arquivo de áudio
        stream.download(output_path=diretorio_destino)

        print(f"O aúdio de '{video.title}' foi baixada com sucesso.")
    
    except Exception as e:
        print(f"Ocorreu um erro ao baixar o seu aúdio: {e}")

if __name__ == "__main__":
    url = input("Digite a URL do vídeo do YouTube: ")
    diretorio = "./audio_files"    

    baixar_musica(url, diretorio)