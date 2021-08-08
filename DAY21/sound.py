from pygame import mixer


def eating_sound():
    mixer.init()
    mixer.music.load("numnumcat.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play()


# r"C:\Users\TOMCAT\Documents\GitHub\100DAY_OF_PYTHON\DAY21\numnumcat.mp3"


def crash_sound():
    mixer.init()
    mixer.music.load("crash.wav")
    mixer.music.set_volume(0.7)
    mixer.music.play()

# r"C:\Users\TOMCAT\Documents\GitHub\100DAY_OF_PYTHON\DAY21\crash.WAV"




