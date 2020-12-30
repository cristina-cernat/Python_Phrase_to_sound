import pyttsx3
import sys
import os

path_input = sys.argv[1]
path_output = sys.argv[2]

for file in os.listdir(path_input):
    if file.endswith(".txt"):
        fd = open(file)
        # print(os.path.splitext(fd.name)[0])
        data = fd.read()
        fd.close()
        engine = pyttsx3.init()
        engine.say(data)
        engine.save_to_file(data, os.path.splitext(fd.name)[0]+".mp3")
        engine.runAndWait()




# file = open("mom.txt")
# data = file.read()
# print(data)
# file.close()

# engine = pyttsx3.init()
# engine.setProperty('rate', 150)
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
# text = data
# engine.say(data)
# # engine.save_to_file(text, 'test2.mp3')
# engine.runAndWait()
