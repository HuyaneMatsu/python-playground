import subprocess, sys

sys.stdout.write('Starting dummy\n')
subprocess.call([sys.executable, 'dummy.py'])

sys.stdout.write('Starting asyncio basic\n')
subprocess.call([sys.executable, 'asyncio_basic.py'])

sys.stdout.write('Starting hata basic\n')
subprocess.call([sys.executable, 'hata_basic.py'])

sys.stdout.write('Starting hata repeat timeout\n')
subprocess.call([sys.executable, 'hata_repeat_timeout.py'])
