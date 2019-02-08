import speech_recognition as sr
from pynput.mouse import Button, Controller

mouse = Controller()
mic = sr.Microphone()
r = sr.Recognizer()
while True:
    with mic as source:
        audio = r.listen(source)

    try:
        best = r.recognize_google(audio)
        print("You said " + best )
        if best == 'open':
            mouse.click(Button.left, 2)
        if best == 'left':
            mouse.click(Button.left, 1)
        if best == 'right':
            mouse.click(Button.right, 1)
    except LookupError:
        print("Could not understand audio")