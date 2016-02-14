#!/usr/bin/python
import Tkinter
import threading
import sys
import evdev
import select
import Queue
import time
import string

letters = []
waitinglist = Queue.Queue()


def convert(code):
    if code == "KEY_Q":
        return 'Q'
    elif code == "KEY_W":
        return 'W'
    elif code == "KEY_E":
        return 'E'
    elif code == "KEY_R":
        return 'R'
    elif code == "KEY_T":
        return 'T'
    elif code == "KEY_Z":
        return 'Z'
    elif code == "KEY_U":
        return 'U'
    elif code == "KEY_I":
        return 'I'
    elif code == "KEY_O":
        return 'O'
    elif code == "KEY_P":
        return 'P'
    elif code == "KEY_A":
        return 'A'
    elif code == "KEY_S":
        return 'S'
    elif code == "KEY_D":
        return 'D'
    elif code == "KEY_F":
        return 'F'
    elif code == "KEY_G":
        return 'G'
    elif code == "KEY_H":
        return 'H'
    elif code == "KEY_J":
        return 'J'
    elif code == "KEY_K":
        return 'K'
    elif code == "KEY_L":
        return 'L'
    elif code == "KEY_Y":
        return 'Y'
    elif code == "KEY_X":
        return 'X'
    elif code == "KEY_C":
        return 'C'
    elif code == "KEY_V":
        return 'V'
    elif code == "KEY_B":
        return 'B'
    elif code == "KEY_N":
        return 'N'
    elif code == "KEY_M":
        return 'M'


class Listener(threading.Thread):

    def __init__(self):
        super(Listener, self).__init__()
        self.done = False

    def run(self):
        dev = evdev.InputDevice(str(sys.argv[1]))
        print(dev)
        while True:
            if self.done is True:
                print "Thread Abbruch.."
                break
            r, w, x = select.select([dev], [], [])
            for event in dev.read():
                if event.type == evdev.ecodes.EV_KEY:
                    input = evdev.categorize(event)
                    if input.keystate:
                        if convert(str(input.keycode)) != None:
                            waitinglist.put(convert(str(input.keycode)))

    def stop(self):
        self.done = True


def draw():
    root.overrideredirect(True)
    root.geometry('+0+100')

    for x in string.ascii_uppercase:
        w = Tkinter.Label(
            root,
            text=x,
            bg="black",
            fg="white",
            font=(
                "Helvetica", 16))
        w.pack(fill=Tkinter.X)
        letters.append(w)


def searchLetter(letter):
    for x in letters:
        if x.cget("text") == letter:
            return letters.index(x)


def stopAfter(label):
    time.sleep(20)
    label.config(bg="black")


def change_color():
    while not waitinglist.empty():
        l = waitinglist.get()
        index = searchLetter(l)
        letters[index].config(bg="white")
        print l, index
        root.after(100, lambda: letters[index].config(bg="black"))
    root.after(5, change_color)


if len(sys.argv) != 2:
    print "Usage: ./letters.py <Path to Keyboard>"
    sys.exit(1)

if not str(sys.argv[1]).startswith('/dev/input/event'):
    print "Error while parsing Argument!\n Stop.."
    sys.exit(1)

root = Tkinter.Tk()
draw()
t = Listener()
t.start()
change_color()
try:
    Tkinter.mainloop()
except:
    print ""
    print "Abbruch.."
    t.stop()
    sys.exit(1)
