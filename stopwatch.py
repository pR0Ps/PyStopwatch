#!/usr/bin/env python

"""Show a basic stopwatch GUI"""

from Tkinter import Button, Frame, Label, Tk, StringVar
from Tkinter import LEFT, NO, TOP, X
import time


class StopWatch(Frame):
    """A frame that tracks and displays elapsed time"""

    def __init__(self, parent=None, **kwargs):
        Frame.__init__(self, parent, kwargs)
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = False

        # Time display
        self.timestr = StringVar()
        Label(self, textvariable=self.timestr).pack(fill=X, expand=NO, pady=2,
                                                    padx=2)
        self._set_time(self._elapsedtime)

        # TK-related
        self._timer = None
        if parent != None:
            parent.title("Stopwatch")

    def _update(self):
        """Update the label with elapsed time"""
        self._elapsedtime = time.time() - self._start
        self._set_time(self._elapsedtime)
        self._timer = self.after(50, self._update)

    def _set_time(self, elap):
        """Set the time string to Minutes:Seconds:Hundreths"""
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))

    def start_stop(self):
        """Start/Stop the stopwatch"""
        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self._set_time(self._elapsedtime)
            self._running = False
        else:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = True

    def reset(self):
        """Reset the stopwatch"""
        self._start = time.time()
        self._elapsedtime = 0.0
        if self._running:
            self.start_stop()
        self._set_time(self._elapsedtime)


def main():
    """Set up the stopwatch and the buttons/keyboard shortcuts to control it"""
    root = Tk()

    # Add stopwatch frame
    stopwatch = StopWatch(root)
    stopwatch.pack(side=TOP)

    # Add buttons
    Button(root, text='Start/Stop',
           command=stopwatch.start_stop, takefocus=False).pack(side=LEFT)
    Button(root, text='Reset',
           command=stopwatch.reset, takefocus=False).pack(side=LEFT)
    Button(root, text='Quit',
           command=root.quit, takefocus=False).pack(side=LEFT)

    # Add keyboard shurtcuts
    root.bind("<space>", lambda x: stopwatch.start_stop())
    root.bind("<BackSpace>", lambda x: stopwatch.reset())
    root.bind("<Escape>", lambda x: root.quit())

    root.focus_set()
    root.mainloop()

if __name__ == '__main__':
    main()
