import subprocess, sys

sys.stdout.write('Starting dummy\n')
subprocess.call([sys.executable, 'dummy.py'])

sys.stdout.write('Starting asyncio basic\n')
subprocess.call([sys.executable, 'asyncio_basic.py'])

sys.stdout.write('Starting scarletio basic\n')
subprocess.call([sys.executable, 'scarletio_basic.py'])

sys.stdout.write('Starting scarletio repeat timeout\n')
subprocess.call([sys.executable, 'scarletio_repeat_timeout.py'])
