import os
import shutil

def cleanDir(dir):
    shutil.rmtree(f'{dir}/logs', ignore_errors=True)
    shutil.rmtree(f'{dir}/output', ignore_errors=True)

    try:
        os.remove(f'{dir}/test-executer')
    except:
        pass
