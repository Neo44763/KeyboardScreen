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
                        key = str(input.keycode).split('_', 1)[1]
                        if key in string.ascii_uppercase:
                            waitinglist.put(key)

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
