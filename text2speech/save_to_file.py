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
                    counter += 1
                    data = line
                    engine = pyttsx3.init()
                    # engine.say(data)
                    final_name = os.path.join(path_output, os.path.splitext(file_name)[0] + str(counter) + ".mp3")
                    engine.save_to_file(data, final_name)

                    engine.runAndWait()
