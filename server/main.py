from backend import Backend
# from gui.MainWindow import MainWindow
import json
import sys
# pylint: disable=no-name-in-module
from gui.gui import GUI
from util.logger import Log

# in-depth memory access violation error logging
import faulthandler
faulthandler.enable()

# with open("./server/config.json", "r") as f:
#     config = json.load(f)

with open("config.json", "r") as f:
    config = json.load(f)

backend = Backend(config["backend"])
gui = GUI(backend)

try:
    Log.info('MAIN', 'Starting application...')

    backend.start()
    gui.run()
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