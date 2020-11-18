# before running this code, be sure to pip install pygame

from pygame import mixer

file = 'iwyback.mp3'

mixer.init()

mixer.music.load(file)

mixer.music.play()

# this provides a delay in closing the program, without it, mixer.music.play() would end the app before playing the song
input("Let it play!")