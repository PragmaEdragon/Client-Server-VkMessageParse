import subprocess
import os
import threading
import time



def createConsoles(filename):
    subprocess.run(f"python {os.path.dirname(os.path.abspath(__file__))}\\{filename}", creationflags=subprocess.CREATE_NEW_CONSOLE)


def createProcess(filename):
    threading.Thread(target=createConsoles, args=(filename,)).start()


if __name__ == '__main__':
    createProcess("server.py")
    time.sleep(1)
    createProcess("main.py")
    time.sleep(1)
    createProcess("user_side.py")
    time.sleep(1)
    createProcess("user_side.py")
