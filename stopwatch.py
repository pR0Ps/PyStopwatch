#!/usr/bin/python

from Tkinter import *
import time

root = None
sw = None

class StopWatch(Frame):  
    """ Implements a stop watch frame widget. """                                                                
    def __init__(self, parent=None, **kw):        
        Frame.__init__(self, parent, kw)
        self._start = 0.0        
        self._elapsedtime = 0.0
        self._running = False
        self.timestr = StringVar()               
        self.makeWidgets()      
        if parent != None:
            parent.title("Stopwatch")

    def makeWidgets(self):                         
        """ Make the time label. """
        l = Label(self, textvariable=self.timestr)
        self._setTime(self._elapsedtime)
        l.pack(fill=X, expand=NO, pady=2, padx=2)                      
    
    def _update(self): 
        """ Update the label with elapsed time. """
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)
    
    def _setTime(self, elap):
        """ Set the time string to Minutes:Seconds:Hundreths """
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)                
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))
        
    def start_stop(self):                                                     
        """ Start/Stop the stopwatch. """
        if self._running:
            self.after_cancel(self._timer)            
            self._elapsedtime = time.time() - self._start    
            self._setTime(self._elapsedtime)
            self._running = False
        else:            
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = True        
    
    def reset(self):                                  
        """ Reset the stopwatch. """
        self._start = time.time()         
        self._elapsedtime = 0.0
        if self._running:
            self.StartStop()
        self._setTime(self._elapsedtime)

# Callbacks for keystrokes
def callbackSS(event):
    sw.start_stop()
def callbackRESET(event):
    sw.reset()
def callbackQUIT(event):
    root.quit()

# Main program
def main():
    global sw, root

    root = Tk()
    sw = StopWatch(root)
    sw.pack(side=TOP)
    
    Button(root, text='Start/Stop', command=sw.start_stop, takefocus=False).pack(side=LEFT)
    Button(root, text='Reset', command=sw.reset, takefocus=False).pack(side=LEFT)
    Button(root, text='Quit', command=root.quit, takefocus=False).pack(side=LEFT)

    root.bind("<space>", callbackSS)
    root.bind("<BackSpace>", callbackRESET)
    root.bind("<Escape>", callbackQUIT)

    root.focus_set()
    root.mainloop()

if __name__ == '__main__':
    main()
