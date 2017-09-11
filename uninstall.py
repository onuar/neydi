import shutil
import os
from pathlib import Path

FILE_NAME = 'tracing.txt'

def uninstall_neydi():
    with open(FILE_NAME) as f:
        data = f.read()
    f.close()

    lines = data.split('\n')
    for line in lines:
        if not line:
            continue
        if os.path.isdir(line):
            shutil.rmtree(folder)
        elif os.path.isfile(line):
            os.remove(line)

        print(f'removed > {line}')

if os.path.isfile(FILE_NAME):
    uninstall_neydi()
else:
    print(f'{FILE_NAME} not found. Are you sure that you installed neydi?')