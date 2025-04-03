
import win32com.client

speaker=win32com.client.Dispatch("SAPI.SpVoice")

fr=open("newfile.txt", "r")
while True:
    line=fr.readline()

    if not line:
        break

    speaker.Speak(line)

print("done")
