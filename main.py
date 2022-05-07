# импорт библиотек
from pydub import AudioSegment
import os
import librosa
import matplotlib.pyplot as plt

# сокращение звука до ровных 4 секунд
def pruning(main_folder):
    # установка пути к ffmpeg
    # AudioSegment.converter = r"C:\\Program Files\\ffmpeg-2.1-win64-static\\bin\\ffmpeg.exe"
    # AudioSegment.ffprobe   = r"C:\\Program Files\\ffmpeg-2.1-win64-static\\bin\\ffprobe.exe"

    # сокращение до 4 секунд
    list_folders = os.listdir(path=f"C:\\Users\\nastydemigod\\Desktop\\kurs\\audio_data\\{main_folder}")
    four_seconds = 4 * 1000
    for folder in list_folders:
        list_notes = os.listdir(path=f"C:\\Users\\nastydemigod\\Desktop\\kurs\\audio_data\\{main_folder}\\{folder}")
        print(f"Сокарщение аудио до 4 секунд в папке: {folder}")
        for note in list_notes:
            song = AudioSegment.from_file(f"C:\\Users\\nastydemigod\\Desktop\\kurs\\audio_data\\{main_folder}\\{folder}\\{note}", "mp3")
            new_song = song[:four_seconds]
            new_song.export(f"C:\\Users\\nastydemigod\\Desktop\\kurs\\audio_data\\{main_folder}\\{folder}\\{note}", format="mp3")

# создание изображений
def get_img(main_folder):
    cmap = plt.get_cmap('inferno')
    list_folders = os.listdir(path=f"C:\\Users\\nastydemigod\\Desktop\\kurs\\img_data\\{main_folder}")
    for folder in list_folders:
        list_notes = os.listdir(path=f"C:\\Users\\nastydemigod\\Desktop\\kurs\\audio_data\\{main_folder}\\{folder}")
        print(f"Создание изображения из аудио в папке: {folder}")
        for note in list_notes:
            song = f"C:\\Users\\nastydemigod\\Desktop\\kurs\\audio_data\\{main_folder}\\{folder}\\{note}"
            img_path = f"C:\\Users\\nastydemigod\\Desktop\\kurs\\img_data\\{main_folder}\\{folder}\\{note[:-4]}.png"
            if os.path.exists(img_path):
                continue
            else:
                x , sr = librosa.load(song, mono=True, duration=4)
                plt.specgram(x, NFFT=2048, Fs=2, Fc=0, noverlap=128, cmap=cmap, sides='default', mode='default', scale='dB')
                plt.axis('off')
                plt.savefig(img_path)
                plt.clf()


if __name__ == '__main__':
    # сокращение звука до ровных 4 секунд на тренировочном наборе
    # pruning("train")

    # сокращение звука до ровных 4 секунд на тестовом
    # pruning("test")

    # создание изображений в тренировочном наборе
    # get_img("train")

    # создание изображений в тестовом наборе
    # get_img("test")
    
    pass
