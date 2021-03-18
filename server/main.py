from .backend import Backend
from .gui import GUI
from time import sleep

backend = Backend(42069)
gui = GUI()

try:
    backend.start()
    gui.start()

    while backend.running or gui.running:
        sleep(0.1)
except (Exception, KeyboardInterrupt) as e:
    if (isinstance(e, KeyboardInterrupt)):
        backend.terminate()
        gui.terminate()

        print("Program Terminated by keyboard...")
    else:
        print("Unexpected error...")