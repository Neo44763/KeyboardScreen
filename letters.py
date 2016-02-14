#!/usr/bin/python
import Tkinter
import threading
import sys
import evdev
import select
import Queue
import time

root = Tkinter.Tk()
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
    w = Tkinter.Label(
        root,
        text="Q",
        bg="black",
        fg="white",
        font=(
            "Helvetica",
         16))
    w.pack(fill=Tkinter.X)
    letters.append(w)
    w = Tkinter.Label(
        root,
        text="W",
        bg="black",
        fg="white",
        font=(
            "Helvetica",
         16))
    w.pack(fill=Tkinter.X)
    letters.append(w)
    w = Tkinter.Label(
        root,
        text="E",
        bg="black",
        fg="white",
        font=(
            "Helvetica",
         16))
    w.pack(fill=Tkinter.X)
    letters.append(w)
    w = Tkinter.Label(
        root,
        text="R",
        bg="black",
        fg="white",
        font=(
            "Helvetica",
         16))
    w.pack(fill=Tkinter.X)
    letters.append(w)
    w = Tkinter.Label(
        root,
        text="T",
        bg="black",
        fg="white",
        font=(
            "Helvetica",
         16))
    w.pack(fill=Tkinter.X)
    letters.append(w)
    w = Tkinter.Label(
        root,
        text="Z",
        bg="black",
        fg="white",
        font=(
            "Helvetica",
         16))
    w.pack(fill=Tkinter.X)
    letters.append(w)
    w = Tkinter.Label(
        root,
        text="U",
        bg="black",
        fg="white",
        font=(
            "Helvetica",
         16))
    w.pack(fill=Tkinter.X)
    letters.append(w)
    w = Tkinter.Label(
        root,
        text="I",
        bg="black",
        fg="white",
        font=(
            "Helvetica",
         16))
    w.pack(fill=Tkinter.X)
    letters.append(w)
    w = Tkinter.Label(
        root,
        text="O",
        bg="black",
        fg="white",
        font=(
            "Helvetica",
         16))
    w.pack(fill=Tkinter.X)
    letters.append(w)
    w = Tkinter.Label(
        root,
        text="P",
        bg="black",
        fg="white",
        font=(
            "Helvetica",
         16))
    w.pack(fill=Tkinter.X)
    letters.append(w)
    w = Tkinter.Label(
        root,
        text="A",
        bg="black",
        fg="white",
        font=(
            "Helvetica",
         16))
    w.pack(fill=Tkinter.X)
    letters.append(w)
    w = Tkinter.Label(
        root,
        text="S",
        bg="black",
        fg="white",
        font=(
            "Helvetica",
         16))
    w.pack(fill=Tkinter.X)
    letters.append(w)
    w = Tkinter.Label(
        root,
        text="D",
        bg="black",
        fg="white",
        font=(
            "Helvetica",
         16))
    w.pack(fill=Tkinter.X)
    letters.append(w)
    w = Tkinter.Label(
        root,
        text="F",
        bg="black",
        fg="white",
        font=(
            "Helvetica",
         16))
    w.pack(fill=Tkinter.X)
    letters.append(w)
    w = Tkinter.Label(
        root,
        text="G",
        bg="black",
        fg="white",
        font=(
            "Helvetica",
         16))
    w.pack(fill=Tkinter.X)
    letters.append(w)
    w = Tkinter.Label(
        root,
        text="H",
        bg="black",
        fg="white",
        font=(
            "Helvetica",
         16))
    w.pack(fill=Tkinter.X)
    letters.append(w)
    w = Tkinter.Label(
        root,
        text="J",
        bg="black",
        fg="white",
        font=(
            "Helvetica",
         16))
    w.pack(fill=Tkinter.X)
    letters.append(w)
    w = Tkinter.Label(
        root,
        text="K",
        bg="black",
        fg="white",
        font=(
            "Helvetica",
         16))
    w.pack(fill=Tkinter.X)
    letters.append(w)
    w = Tkinter.Label(
        root,
        text="L",
        bg="black",
        fg="white",
        font=(
            "Helvetica",
         16))
    w.pack(fill=Tkinter.X)
    letters.append(w)
    w = Tkinter.Label(
        root,
        text="Y",
        bg="black",
        fg="white",
        font=(
            "Helvetica",
         16))
    w.pack(fill=Tkinter.X)
    letters.append(w)
    w = Tkinter.Label(
        root,
        text="X",
        bg="black",
        fg="white",
        font=(
            "Helvetica",
         16))
    w.pack(fill=Tkinter.X)
    letters.append(w)
    w = Tkinter.Label(
        root,
        text="C",
        bg="black",
        fg="white",
        font=(
            "Helvetica",
         16))
    w.pack(fill=Tkinter.X)
    letters.append(w)
    w = Tkinter.Label(
        root,
        text="V",
        bg="black",
        fg="white",
        font=(
            "Helvetica",
         16))
    w.pack(fill=Tkinter.X)
    letters.append(w)
    w = Tkinter.Label(
        root,
        text="B",
        bg="black",
        fg="white",
        font=(
            "Helvetica",
         16))
    w.pack(fill=Tkinter.X)
    letters.append(w)

    w = Tkinter.Label(
        root,
        text="N",
        bg="black",
        fg="white",
        font=(
            "Helvetica",
         16))
    w.pack(fill=Tkinter.X)
    letters.append(w)
    w = Tkinter.Label(
        root,
        text="M",
        bg="black",
        fg="white",
        font=(
            "Helvetica",
         16))
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


draw()
t = Listener()
t.start()
change_color()
try:
    Tkinter.mainloop()
except (KeyboardInterrupt, SystemExit):
    print ""
    print "Abbruch.."
    t.stop()
    sys.exit(1)
