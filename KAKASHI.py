import os, sys
os.system("git pull")
try:
    __import__("Hyphex").ARIYAN()
except Exception as e:
    exit(str(e))
