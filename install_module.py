import pip
import os
fo = open(os.path.join(os.path.dirname(__file__), 'requirements.txt'), "r")
inp = fo.read()
ls = inp.split()

for i in ls:
    pip.main(['install', i])
