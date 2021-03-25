from backend import Backend
from gui.MainWindow import MainWindow
from time import sleep
import json
import sys
# pylint: disable=no-name-in-module
from util.logger import Log

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from PyQt5.uic import loadUi

import faulthandler
faulthandler.enable()

with open("./server/config.json", "r") as f:
    config = json.load(f)

port = config["backend"]["port"]
password = config["moderator"]["password"]

backend = Backend(port)
app = QApplication(sys.argv)
gui = MainWindow(backend)
gui.show()


try:
    Log.info('MAIN', 'Starting application...')

    backend.start()
    # gui.start()

    # app.exec()
    sys.exit(app.exec())

    while backend.running or gui.running:
        sleep(0.1)
except (Exception, KeyboardInterrupt) as e:
    if (isinstance(e, KeyboardInterrupt)):
        Log.info('MAIN', 'Received keyboard interrupt')
    else:
        print("Unexpected error...")

        print(e)
finally:
    backend.terminate()
    gui.terminate()

    sys.exit()

