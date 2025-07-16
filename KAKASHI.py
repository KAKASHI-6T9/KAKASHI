import os, sys
os.system("git pull")
try:
    __import__("Hyphex.py").ARIYAN()
except Exception as e:
    exit(str(e))
