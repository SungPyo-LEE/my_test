import sys
import os

CURRENT_DIR = os.getcwd()

sys.stdout = sys.stderr
sys.path.inser(0, CURRENT_DIR)

from app import app as application
