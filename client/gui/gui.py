from PyQt5.QtWidgets import QApplication
import sys
# pylint: disable=no-name-in-module
from gui.MainWindow import MainWindow
from util.logger import Log

class GUI():
    def __init__(self, backend):
        self._running = True

        self.backend = backend

    @property
    def running(self):
        return self._running

    def run(self):
        Log.info('GUI', 'Running')
        
        self.app = QApplication(sys.argv)
        self.main_window = MainWindow(self.backend)

        # open our main window and start the app
        self.main_window.show()
        self.app.exec()

        self.backend.terminate()
        self.terminate()

    def terminate(self):
        if self._running:
            Log.info('GUI', 'Terminating...')

            self._running = False