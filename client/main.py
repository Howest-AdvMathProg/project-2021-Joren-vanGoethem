from backend import Backend
from gui.gui import GUI
from time import sleep
import json
import sys
# pylint: disable=no-name-in-module
from util.logger import Log

with open("config.json", "r") as f:
    config = json.load(f)

host = config["backend"]["host"]
port = config["backend"]["port"]

backend = Backend(host, port)
gui = GUI(backend)

Log.log_level = 'INFO'

try:
    Log.info('MAIN', 'Starting application...')

    backend.start()
    gui.run()

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
