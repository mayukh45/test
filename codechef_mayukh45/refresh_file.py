from time import sleep
from codechef_mayukh45.MAIN import generate_refresh_token
import sys
import importlib
#from conf import refresh_token

import os
#os.path.append('/home/mayukh/Documents/codechef_mayukh45')

def refresh():

    while(True):
        from conf import refresh_token
        del sys.modules['conf']
        f = open('conf.py','r')
        print(f.read())
        print(refresh_token)

        generate_refresh_token(refresh_token)
        sleep(20*60)
        sys.stdout.flush()

refresh()