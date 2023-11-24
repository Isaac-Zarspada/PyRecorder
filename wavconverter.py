#choose image from local storage
from pydub import AudioSegment
from tkinter.filedialog import *

# file_path=askopenfilename()

sound = AudioSegment.from_wav(r"C:\Code\output.wav")
sound.export(r"C:\Users\isaac\Music\output.mp3", format="mp3")
