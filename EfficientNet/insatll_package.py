import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'gpiozero'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pigpio'])
