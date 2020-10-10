import os
from glob import glob
from random import choice
from moviepy.editor import *


audio_dir="D:\\songs\\"
image_dir ="D:\\songs\\images\\"
image_choice = []



def select_audio(audio_dir):
    result = [y for x in os.walk(audio_dir) for y in glob(os.path.join(x[0], '*.mp3'))]
    return result

def random_image():
    for root, dirs, files in os.walk(image_dir):
        for f in files:
            fullpath = os.path.join(root, f)
            image_choice.append(fullpath)
    return choice(image_choice)


def render_video():
    for audio_path in select_audio(audio_dir):
        a = audio_path
        b = audio_path
        audio = AudioFileClip(audio_path)
        name = a.split('\\')[-1].split('.')[0] +" "+ b.split('\\')[-2]+".mp4"

        clip = ImageClip(random_image()).set_duration(audio.duration)
        clip = clip.set_audio(audio)
        clip.write_videofile(name, fps=24)

render_video()








# def audio_select():
#     for root, dirs, files in os.walk(audio_dir):
#         for f in files:
#             if os.path.splitext(f)[1] == '.mp3':
#                 fullpath = os.path.join(root, f)
#                 print(fullpath)
#                 audio = AudioFileClip(fullpath)

# for file in os.listdir(fpath):
#     if file.endswith(".mp3"):
#         print(os.path.join(fpath, file))

        # audio = AudioFileClip(sname)
        # clip = ImageClip("D:\\songs\\images\\1.png").set_duration(audio.duration)
        # clip = clip.set_audio(audio)
        # name=file[:-4]+".mp4"
        # print(name)
        # clip.write_videofile(name, fps=24)

