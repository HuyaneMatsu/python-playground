import subprocess, sys

sys.stdout.write('Starting asyncio benchmark\n')
subprocess.call([sys.executable, 'asyncio_benchmark.py'])

sys.stdout.write('Starting scarletio old benchmark\n')
subprocess.call([sys.executable, 'scarletio_old_benchmark.py'])

sys.stdout.write('Starting scarletio new benchmark\n')
subprocess.call([sys.executable, 'scarletio_new_benchmark.py'])
