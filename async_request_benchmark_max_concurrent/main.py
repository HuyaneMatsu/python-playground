import subprocess, sys

sys.stdout.write('Starting scarletio benchmark\n')
subprocess.call([sys.executable, 'scarletio_benchmark.py'])

sys.stdout.write('Starting asyncio + aiohttp benchmark\n')
subprocess.call([sys.executable, 'asyncio_benchmark.py'])
