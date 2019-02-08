import speech_recognition as sr
from pynput.mouse import Button, Controller

mouse = Controller()
mic = sr.Microphone()
r = sr.Recognizer()
nextc = True
i = 0
while True:
    if i > 100:
        print(i)
        i = 0
        nextc = True
    while nextc:
        try:
            with mic as source:
                audio = r.listen(source)

        except:
            print('error')

        try:
            best = r.recognize_google(audio)
            print("You said " + best )
            if best == 'open':
                mouse.click(Button.left, 2)
            if best == 'left':
                mouse.click(Button.left, 1)
            if best == 'right':
                mouse.click(Button.right, 1)
            nextc = False
        except LookupError:
            print("Could not understand audio")
    print(i)
    i += 1