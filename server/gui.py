 import threading

class GUI(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
        self._running = True

    @property
    def running(self):
        return self._running

    def run(self):
        
        while self._running:
            pass