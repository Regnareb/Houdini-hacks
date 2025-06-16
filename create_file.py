import os
import platform

if platform.system() == 'Windows':
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
else:
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
with open(os.path.join(desktop, 'houdini_hacked.txt'), 'w') as f:
    f.write('All your files belong to us')
