import os
import random
import socket
import time
import subprocess

os.system("ln -s /home/mistake/flag flag")

stdinr, stdinw = os.pipe()
stderrr, stderrw = os.pipe()

os.write(stdinw, "\x00"*10 + "\x01"*10)
pro = subprocess.Popen(["/home/mistake/mistake"], stdin=stdinr)

# flag: Mommy, the operator priority always confuses me :(
