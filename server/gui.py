import threading
# pylint: disable=no-name-in-module
from util.logger import Log

class GUI(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        
        self._running = True

    @property
    def running(self):
        return self._running

    def run(self):
        Log.info('GUI', 'Running')
        
        while self._running:
            pass

    def terminate(self):
        Log.info('GUI', 'Terminating...')

        self._running = False