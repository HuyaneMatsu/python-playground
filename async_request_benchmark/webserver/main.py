from time import sleep
import subprocess, sys

processes = [
    subprocess.Popen([sys.executable, 'app.py', str(port)], stdout=subprocess.DEVNULL)
    for port in range(100, 105)
]


try:
    while True:
        sleep(600)
except KeyboardInterrupt:
    for process in processes:
        process.kill()
    
    raise
