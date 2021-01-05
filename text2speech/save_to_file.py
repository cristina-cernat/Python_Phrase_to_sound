import pyttsx3
import sys
import os

path_input = sys.argv[1]
path_output = sys.argv[2]


for (root, dirs, files) in os.walk(path_input):
    for file_name in files:
        file_name_absolute = os.path.join(root, file_name)
        with open(file_name_absolute, encoding="utf8") as fd:
            counter = 0
            for line in fd.readlines():
                if line.strip():
                    # data = fd.read()
                    counter += 1
                    data = line
                    engine = pyttsx3.init()
                    # engine.say(data)

                    final_name = os.path.join(path_output, os.path.splitext(file_name)[0] + str(counter) + ".mp3")
                    engine.save_to_file(data, final_name)

                    engine.runAndWait()

# for (root, dirs, files) in os.walk("."):
#     for file in files:
#         full_fileName = os.path.join(root, file)
#         print(full_fileName)


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
